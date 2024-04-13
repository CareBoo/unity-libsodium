import os
import sys
import shutil
import re

INCLUDE_PTN = re.compile(r'#\s*include\s+"(.*)"')
FILENAME_SEP = "___"
DIR_SEP = "_"

def compute_new_filename(relative_path, filename):
    if relative_path == ".":
        return f"{FILENAME_SEP}{filename}"
    else:
        return f"{relative_path.replace(os.sep, DIR_SEP)}{FILENAME_SEP}{filename}"
    

def local_include_path(flattened_filename, include_path):
    reldir, _ = flattened_filename.split(FILENAME_SEP)
    include_path_split = reldir.split(DIR_SEP) + include_path.split(os.sep)
    include_path_split = os.path.normpath(os.path.join(*include_path_split)).split(os.sep)
    include_dirs = DIR_SEP.join(include_path_split[:-1])
    include_name = include_path_split[-1]
    
    return f"{include_dirs}{FILENAME_SEP}{include_name}"


def global_include_path(include_path):
    include_path_split = ['include', 'sodium'] + include_path.split(os.sep)
    include_dirs = DIR_SEP.join(include_path_split[:-1])
    include_name = include_path_split[-1]

    return f"{include_dirs}{FILENAME_SEP}{include_name}"


def flatten_directory(source_directory, output_directory, includes):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    for root, dirs, files in os.walk(source_directory):
        for filename in files:
            is_c = filename.endswith(".c")
            is_h = filename.endswith(".h")
            if not is_c and not is_h:
                continue
            relative_path = os.path.relpath(root, source_directory)
            new_filename = compute_new_filename(relative_path, filename)

            if is_h:
                includes.add(new_filename)
            
            # Construct the full source and destination paths
            source_path = os.path.join(root, filename)
            destination_path = os.path.join(output_directory, new_filename)
            
            # Copy the file to the new location with the flattened name
            shutil.copy2(source_path, destination_path)


def update_includes(root, filename, includes):
    def replace_include(match):
        original_path = match.group(1)
        local_new_path = local_include_path(filename, original_path)
        if local_new_path in includes:
            return f'#include "{local_new_path}"'
        global_new_path = global_include_path(original_path)
        if global_new_path in includes:
            return f'#include "{global_new_path}"'
        print(f"WARNING: Could not find include {original_path} in includes in {filename}")
        return match.group(0)
    
    file_path = os.path.join(root, filename)
    with open(file_path, "r") as f:
        content = f.read()
    new_content = re.sub(INCLUDE_PTN, replace_include, content)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python flatten.py <source_directory> <output_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    output_directory = sys.argv[2]
    includes = set()
    flatten_directory(source_directory, output_directory, includes)

    for root, _, files in os.walk(output_directory):
        for filename in files:
            update_includes(root, filename, includes)

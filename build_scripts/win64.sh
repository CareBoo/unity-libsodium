wget https://download.libsodium.org/libsodium/releases/libsodium-1.0.18-msvc.zip
unzip libsodium-1.0.18-msvc.zip -d msvc

mkdir -p output/builds
basedir=msvc/libsodium/x64/Debug/v140/dynamic
cp $basedir/libsodium.dll $basedir/libsodium.pdb output/builds

#!/bin/sh

cd libsodium
if [ -f "dist-build/macos.sh" ]; then
    mac_name="macos"
else
    mac_name="osx"
fi
./dist-build/${mac_name}.sh

cd -
mkdir -p output/builds/MacOS
cp libsodium/libsodium-${mac_name}/lib/libsodium.*.dylib output/builds/sodium.bundle

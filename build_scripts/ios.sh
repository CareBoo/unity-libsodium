#!/bin/sh

cd libsodium
./dist-build/ios.sh

cd -
mkdir -p output/builds
cp libsodium/libsodium-ios/lib/libsodium.a output/builds/libsodium.a

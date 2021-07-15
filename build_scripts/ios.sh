#!/bin/sh

cd libsodium
./dist-build/ios.sh

cd -
mkdir -p output/builds/iOS
cp libsodium/libsodium-ios/lib/libsodium.a output/builds/iOS/libsodium.a

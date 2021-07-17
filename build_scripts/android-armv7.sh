#!/bin/sh

export ANDROID_NDK_HOME="$(pwd)/android-ndk"
mkdir ANDROID_NDK_HOME

mkdir temp_dir
cd temp_dir
wget -q https://dl.google.com/android/repository/android-ndk-r13b-darwin-x86_64.zip
unzip -o -q android-ndk-r13b-darwin-x86_64.zip
mv android-ndk-r13b ${ANDROID_NDK_HOME}
cd -

cd libsodium
./dist-build/android-armv7-a.sh
cd -

mkdir -p output/builds/Android/armv7
mv libsodium/libsodium-android-armv7-a/lib/libsodium.a libsodium/libsodium-android-armv7-a/lib/libsodium.so output/builds

#!/bin/sh

cd libsodium
./configure --host=x86-pc-linux-gnu
make && make check

cd -
mkdir -p output/builds
cp libsodium/src/libsodium/.libs/libsodium.so output/builds/libsodium.so

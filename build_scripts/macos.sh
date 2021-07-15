#!/bin/sh

cd libsodium
if [ -f "dist-build/macos.sh" ]; then
    ./dist-build/macos.sh
else
    ./dist-build/osx.sh
fi

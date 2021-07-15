# unity-libsodium

I'm just using this to build libsodium via Github Actions, since I do not own a mac device :X.

# How to run a build
1. Go to the Actions tab
2. Click on the "Create Plugins" workflow
3. Manually run the workflow by clicking on "Run workflow" button
4. Enter the libsodium tag you'd like to build. (hint: this is the version, e.g. 1.0.18)
5. The workflow will run, and likely fail, because this repository is meant to build 1.0.18...
6. Wait for me to add libsodium as a submodule to this repo so the version is pinned and any update to the main branch triggers a build so you don't have to do all this stuff anymore.

Useful references:
- https://github.com/netpyoung/unity.libsodium
- https://github.com/jedisct1/libsodium

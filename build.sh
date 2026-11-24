#!/usr/bin/env bash
set -euo pipefail

# Fetch the upstream app at build time so Render serves the actual application,
# not a placeholder. Pinning the upstream repository's main branch keeps updates
# reproducible per Render build and makes the source relationship explicit.
rm -rf .build/barehands
mkdir -p .build
git clone --depth 1 https://github.com/jaredrhod/barehands.git .build/barehands
test -f .build/barehands/stage.html
test -f .build/barehands/server.py
printf 'Fetched Barehands source revision: '
git -C .build/barehands rev-parse --short HEAD

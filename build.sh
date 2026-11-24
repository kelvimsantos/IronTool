#!/usr/bin/env bash
set -euo pipefail

# Fetch the upstream app at build time so Render serves the actual application.
rm -rf .build/barehands
mkdir -p .build
git clone --depth 1 https://github.com/jaredrhod/barehands.git .build/barehands
test -f .build/barehands/stage.html
test -f .build/barehands/server.py

# Include assets committed to this IronTool repository in the deployed app.
# Render's filesystem is ephemeral, so the repository is the durable source.
if [ -d media ]; then
  mkdir -p .build/barehands/media
  cp -R media/. .build/barehands/media/
fi

printf 'Fetched Barehands source revision: '
git -C .build/barehands rev-parse --short HEAD

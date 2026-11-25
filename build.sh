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

# Fetch a few recognizable GLB samples at build time instead of committing
# large binary assets. Pin the source revision so deployments are reproducible.
ASSET_REV=e124e8d8d7330a5372bc2b4d00d39a4d9d7997ea
MODEL_DIR=.build/barehands/media/models
mkdir -p "$MODEL_DIR"
fetch_model() {
  local source_path="$1"
  local filename="$2"
  curl --fail --location --retry 2 \
    "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/${ASSET_REV}/Models/${source_path}" \
    --output "$MODEL_DIR/$filename"
  test -s "$MODEL_DIR/$filename"
}
fetch_model "Fox/glTF-Binary/Fox.glb" "fox-character.glb"
fetch_model "CarConcept/glTF-Binary/CarConcept.glb" "car-concept.glb"
fetch_model "CesiumMilkTruck/glTF-Binary/CesiumMilkTruck.glb" "cesium-milk-truck.glb"

printf 'Fetched Barehands source revision: '
git -C .build/barehands rev-parse --short HEAD

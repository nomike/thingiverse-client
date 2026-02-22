#!/usr/bin/env bash
# Bundle the OpenAPI spec with Redocly, then generate the Python client with openapi-python-client.
# Prerequisite: openapi/ must be populated (run scripts/fetch_openapi_spec.py first).
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OPENAPI_DIR="$REPO_ROOT/openapi"
BUNDLED="$OPENAPI_DIR/bundled.yaml"
OUTPUT_DIR="$REPO_ROOT/thingiverse_client"
CONFIG="$OPENAPI_DIR/generator-config.yaml"

cd "$REPO_ROOT"

if [[ ! -f "$OPENAPI_DIR/openapi.yaml" ]]; then
  echo "openapi/openapi.yaml not found. Run scripts/fetch_openapi_spec.py first to download the spec."
  exit 1
fi

echo "Bundling OpenAPI spec with Redocly..."
npx --yes @redocly/cli bundle "$OPENAPI_DIR/openapi.yaml" -o "$BUNDLED" --component-renaming-conflicts-severity off

echo "Applying upstream-spec fixes (descriptions, array items, path params, path templating)..."
python "$SCRIPT_DIR/patch_bundled_spec_full.py" "$BUNDLED"

echo "Generating Python client..."
TMPDIR="$(mktemp -d)"
TEMP_OUTPUT="$TMPDIR/thingiverse-client"
openapi-python-client generate --path "$BUNDLED" --config "$CONFIG" --output-path "$TEMP_OUTPUT"

# The generator creates a full project; we only want the inner package.
if [[ ! -d "$TEMP_OUTPUT/thingiverse_client" ]]; then
  echo "Error: expected package dir $TEMP_OUTPUT/thingiverse_client not found."
  rm -rf "$TMPDIR"
  exit 1
fi

rm -rf "$OUTPUT_DIR"
mv "$TEMP_OUTPUT/thingiverse_client" "$OUTPUT_DIR"
rm -rf "$TMPDIR"

echo "Done. Client is in $OUTPUT_DIR"

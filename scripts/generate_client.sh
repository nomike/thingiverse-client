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
GEN_TMPDIR="$(mktemp -d)"
TEMP_OUTPUT="$GEN_TMPDIR/thingiverse-client"
openapi-python-client generate --path "$BUNDLED" --config "$CONFIG" --output-path "$TEMP_OUTPUT"

# The generator creates a full project; we only want the inner package.
if [[ ! -d "$TEMP_OUTPUT/thingiverse_client" ]]; then
  echo "Error: expected package dir $TEMP_OUTPUT/thingiverse_client not found."
  rm -rf "$GEN_TMPDIR"
  exit 1
fi

rm -rf "$OUTPUT_DIR"
mv "$TEMP_OUTPUT/thingiverse_client" "$OUTPUT_DIR"
rm -rf "$GEN_TMPDIR"

# Add project-specific constants that the generator does not produce.
cat > "$OUTPUT_DIR/_constants.py" << 'PYEOF'
"""Thingiverse API base URLs (not part of the generated client)."""

BASE_URL_PRODUCTION: str = "https://api.thingiverse.com"
BASE_URL_STAGING: str = "https://api-staging.thingiverse.com"
PYEOF

# Re-export the constants from the package __init__.
if ! grep -q "BASE_URL_PRODUCTION" "$OUTPUT_DIR/__init__.py"; then
  python -c "
import pathlib, sys
p = pathlib.Path(sys.argv[1])
t = p.read_text()
t = t.replace(
    'from .client import',
    'from ._constants import BASE_URL_PRODUCTION, BASE_URL_STAGING\nfrom .client import',
    1,
)
t = t.replace(
    '__all__ = (',
    '__all__ = (\n    \"BASE_URL_PRODUCTION\",\n    \"BASE_URL_STAGING\",',
    1,
)
p.write_text(t)
" "$OUTPUT_DIR/__init__.py"
fi

echo "Done. Client is in $OUTPUT_DIR"

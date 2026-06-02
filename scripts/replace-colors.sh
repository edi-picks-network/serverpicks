#!/bin/bash
# Batch color and branding replacement for emailmarketing-tools-hub
# Red theme conversion

APP_DIR="/home/edi/emailmarketing-tools-hub/app"

# ===== COLOR REPLACEMENTS =====
# #3B82F6 (blue) -> #E63946 (red)
# #22D3EE (cyan) -> #FF6B6B (rose)
# #2563EB (blue hover) -> #C53030 (dark red)
# #0A1628 (deep bg) -> #1A0A0A (dark red bg)
# #0F1D32 (secondary bg) -> #2D0F0F
# #162440 (tertiary bg) -> #401616
# #1E3A5F (border subtle) -> #5F1E1E
# #2A5080 (border active) -> #802828
# #F0F4F8 (text primary) -> #FEF2F0
# #8BA3BE (text secondary) -> #BE8A83
# #4A6380 (text muted) -> #80504A

echo "Starting batch color replacement..."

# Process all .tsx, .ts, .css files in app directory
find "$APP_DIR" -type f \( -name "*.tsx" -o -name "*.ts" -o -name "*.css" \) | while read file; do
  # Skip node_modules and .next
  if echo "$file" | grep -q "node_modules\|\.next"; then
    continue
  fi
  
  sed -i \
    -e 's/#3B82F6/#E63946/g' \
    -e 's/#22D3EE/#FF6B6B/g' \
    -e 's/#2563EB/#C53030/g' \
    -e 's/#0A1628/#1A0A0A/g' \
    -e 's/#0F1D32/#2D0F0F/g' \
    -e 's/#162440/#401616/g' \
    -e 's/#1E3A5F/#5F1E1E/g' \
    -e 's/#2A5080/#802828/g' \
    -e 's/#F0F4F8/#FEF2F0/g' \
    -e 's/#8BA3BE/#BE8A83/g' \
    -e 's/#4A6380/#80504A/g' \
    "$file"
    
  echo "  Processed: $file"
done

echo "Color replacement complete!"

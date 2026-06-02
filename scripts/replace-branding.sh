#!/bin/bash
# Batch branding replacement for emailmarketing-tools-hub

APP_DIR="/home/edi/emailmarketing-tools-hub/app"

echo "Starting branding replacement..."

find "$APP_DIR" -type f \( -name "*.tsx" -o -name "*.ts" \) | while read file; do
  if echo "$file" | grep -q "node_modules\|\.next\|blog-posts\|blog_new_entry\|new-tools-batch"; then
    continue
  fi
  
  sed -i \
    -e 's/B2B Software List/Email Marketing Tools Hub/g' \
    -e 's/B2B SaaS Hub/Email Marketing Hub/g' \
    -e 's/SaaS Hub/Email Hub/g' \
    -e 's/B2B SaaS/email marketing/g' \
    -e 's/B2B software/email marketing software/g' \
    -e 's/B2B solutions/email marketing solutions/g' \
    -e 's/enterprise software/email marketing software/g' \
    -e 's/Enterprise Software/Email Marketing Software/g' \
    -e 's/Enterprise Tool/Email Marketing Tool/g' \
    -e 's/enterprise tools/email marketing tools/g' \
    -e 's/Enterprise Tools/Email Marketing Tools/g' \
    -e 's/enterprise SaaS/email marketing/g' \
    -e 's/business software/email marketing software/g' \
    -e 's/Business Software/Email Marketing Software/g' \
    -e 's/5000+ Business Tools/200+ Email Marketing Tools/g' \
    -e 's/5000+/200+/g' \
    "$file"
    
  echo "  Processed: $file"
done

echo "Branding replacement complete!"

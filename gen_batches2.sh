#!/bin/bash
QWEN_KEY1=$(python3 -c "
with open('/home/edi/.hermes/api_keys.env') as f:
    for line in f:
        if line.startswith('QWEN_API_KEY_1='):
            print(line.strip().split('=',1)[1])
            break
")
API_URL="https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
OUTPUT_DIR="/tmp/serverpicks_batches"
mkdir -p $OUTPUT_DIR

echo "=== Batch 3: CDN & DNS ==="
curl -s --connect-timeout 15 --max-time 120 -X POST "$API_URL" \
  -H "Authorization: Bearer $QWEN_KEY1" \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen-plus","messages":[{"role":"user","content":"Return a JSON array of 10 CDN/DNS tools. Each object: id, name, category=\"CDN & DNS\", rating, reviewCount, description, longDescription, pros[5], cons[3], pricing, pricingDetail, features[6], useCase, websiteUrl, alternatives[3], scoreBreakdown{\"features\":N,\"reviews\":N,\"momentum\":N,\"popularity\":N}, userQuotes[2]{\"role\",\"company\",\"quote\"}. Tools: cloudflare/Akamai/Fastly/KeyCDN/Bunny.net/StackPath/Amazon CloudFront/Google Cloud CDN/Azure CDN/NS1"}],"max_tokens":8000,"temperature":0.7}' > $OUTPUT_DIR/batch3.json 2>&1

echo "=== Batch 4: Domain & SSL ==="
curl -s --connect-timeout 15 --max-time 120 -X POST "$API_URL" \
  -H "Authorization: Bearer $QWEN_KEY1" \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen-plus","messages":[{"role":"user","content":"Return a JSON array of 10 domain/SSL tools. Same format. Tools: GoDaddy/Namecheap/Porkbun/Cloudflare Registrar/Amazon Route 53/Google Cloud DNS/Azure DNS/Lets Encrypt/Sectigo/SSL.com. Category=\"Domain & SSL\""}],"max_tokens":8000,"temperature":0.7}' > $OUTPUT_DIR/batch4.json 2>&1

echo "=== Batch 5: Server Mgmt ==="
curl -s --connect-timeout 15 --max-time 120 -X POST "$API_URL" \
  -H "Authorization: Bearer $QWEN_KEY1" \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen-plus","messages":[{"role":"user","content":"Return a JSON array of 10 server management tools. Same format. Tools: cPanel/Plesk/Webmin/Cockpit/Ansible/Puppet/Chef/Terraform/Pulumi/Salt Project. Category=\"Server Management & DevOps\""}],"max_tokens":8000,"temperature":0.7}' > $OUTPUT_DIR/batch5.json 2>&1

echo "=== Batch 6: Monitoring & DB ==="
curl -s --connect-timeout 15 --max-time 120 -X POST "$API_URL" \
  -H "Authorization: Bearer $QWEN_KEY1" \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen-plus","messages":[{"role":"user","content":"Return a JSON array of 10 monitoring/database hosting tools. Same format. Tools: Grafana/Prometheus/Datadog/New Relic/MongoDB Atlas/Amazon RDS/PlanetScale/Supabase/Neon/Railway. Category=\"Monitoring & Databases\""}],"max_tokens":8000,"temperature":0.7}' > $OUTPUT_DIR/batch6.json 2>&1

echo "=== Done ==="
for f in $OUTPUT_DIR/batch*.json; do
  python3 -c "import json; d=json.load(open('$f')); print(f'$(basename $f): {len(json.loads(d[\"choices\"][0][\"message\"][\"content\"]))} tools')" 2>&1
done

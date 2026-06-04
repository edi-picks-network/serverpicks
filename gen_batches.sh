#!/bin/bash
# Generate serverpicks tools data - batch by batch
# Using curl instead of Python for reliability

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

# Batch 1: Cloud Platforms (10 tools)
echo "=== Batch 1: Cloud Platforms ==="
cat > /tmp/payload1.json << 'PAYLOAD'
{"model":"qwen-plus","messages":[{"role":"user","content":"Generate 10 cloud platform tools. Return ONLY a JSON array. Each object: id, name (real name), category=\"Cloud Platforms\", rating(3.5-5.0), reviewCount(100-5000), description(30 words), longDescription(60 words), pros[5], cons[3], pricing, pricingDetail(15 words), features[6], useCase, websiteUrl, alternatives[3], scoreBreakdown{\"features\":N,\"reviews\":N,\"momentum\":N,\"popularity\":N}, userQuotes[2]{\"role\",\"company\",\"quote\"}. Tools: [{\"id\":\"aws\",\"name\":\"Amazon Web Services\"},{\"id\":\"azure\",\"name\":\"Microsoft Azure\"},{\"id\":\"gcp\",\"name\":\"Google Cloud Platform\"},{\"id\":\"digitalocean\",\"name\":\"DigitalOcean\"},{\"id\":\"linode\",\"name\":\"Linode\"},{\"id\":\"vultr\",\"name\":\"Vultr\"},{\"id\":\"alibaba-cloud\",\"name\":\"Alibaba Cloud\"},{\"id\":\"oracle-cloud\",\"name\":\"Oracle Cloud Infrastructure\"},{\"id\":\"ibm-cloud\",\"name\":\"IBM Cloud\"},{\"id\":\"tencent-cloud\",\"name\":\"Tencent Cloud\"}]"}],"max_tokens":8000,"temperature":0.7}
PAYLOAD
curl -s --connect-timeout 15 --max-time 120 -X POST "$API_URL" \
  -H "Authorization: Bearer $QWEN_KEY1" \
  -H "Content-Type: application/json" \
  -d @/tmp/payload1.json > $OUTPUT_DIR/batch1.json 2>&1
python3 -c "import json; d=json.load(open('$OUTPUT_DIR/batch1.json')); print(f'Batch 1: {len(json.loads(d[\"choices\"][0][\"message\"][\"content\"]))} tools')" 2>&1 || echo "Batch 1: parse error"

# Batch 2: VPS & Dedicated Servers (10 tools)
echo "=== Batch 2: VPS & Dedicated ==="
cat > /tmp/payload2.json << 'PAYLOAD'
{"model":"qwen-plus","messages":[{"role":"user","content":"Generate 10 VPS/dedicated server tools. Return ONLY JSON array. Same format as before. Tools: [{\"id\":\"hetzner\",\"name\":\"Hetzner\"},{\"id\":\"ovhcloud\",\"name\":\"OVHcloud\"},{\"id\":\"contabo\",\"name\":\"Contabo\"},{\"id\":\"scaleway\",\"name\":\"Scaleway\"},{\"id\":\"ionos\",\"name\":\"IONOS Cloud\"},{\"id\":\"upcloud\",\"name\":\"UpCloud\"},{\"id\":\"civo\",\"name\":\"Civo\"},{\"id\":\"kamatera\",\"name\":\"Kamatera\"},{\"id\":\"greencloudvps\",\"name\":\"GreenCloudVPS\"},{\"id\":\"interserver\",\"name\":\"InterServer\"}] Category: \"VPS & Dedicated Servers\"."}],"max_tokens":8000,"temperature":0.7}
PAYLOAD
curl -s --connect-timeout 15 --max-time 120 -X POST "$API_URL" \
  -H "Authorization: Bearer $QWEN_KEY1" \
  -H "Content-Type: application/json" \
  -d @/tmp/payload2.json > $OUTPUT_DIR/batch2.json 2>&1
python3 -c "import json; d=json.load(open('$OUTPUT_DIR/batch2.json')); print(f'Batch 2: {len(json.loads(d[\"choices\"][0][\"message\"][\"content\"]))} tools')" 2>&1 || echo "Batch 2: parse error"

echo "=== Done ==="

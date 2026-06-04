#!/bin/bash
QWEN_KEY1=$(python3 -c "
with open('/home/edi/.hermes/api_keys.env') as f:
    for line in f:
        if line.startswith('QWEN_API_KEY_1='):
            print(line.strip().split('=',1)[1])
            break
")
API_URL="https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
curl -s --connect-timeout 15 --max-time 120 -X POST "$API_URL" \
  -H "Authorization: Bearer $QWEN_KEY1" \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen-plus","messages":[{"role":"user","content":"Return a JSON array of 10 CDN/DNS tools. Each object: id, name, category=\"CDN & DNS\". Fields: rating, reviewCount, description, longDescription, pros[5], cons[3], pricing, pricingDetail, features[6], useCase, websiteUrl, alternatives[3], scoreBreakdown, userQuotes[2]. Tools: Cloudflare, Akamai, Fastly, KeyCDN, Bunny.net, StackPath, Amazon CloudFront, Google Cloud CDN, Azure CDN, NS1"}],"max_tokens":8000,"temperature":0.7}' > /tmp/serverpicks_batches/batch3.json 2>&1
python3 -c "import json; d=json.load(open('/tmp/serverpicks_batches/batch3.json')); print(f'Batch 3: {len(json.loads(d[\"choices\"][0][\"message\"][\"content\"]))} tools')" 2>&1

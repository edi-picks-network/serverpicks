#!/usr/bin/env python3
import urllib.request, json

key = None
with open('/home/edi/.hermes/api_keys.env') as f:
    for line in f:
        if line.startswith('QWEN_API_KEY_1='):
            key = line.strip().split('=', 1)[1]
            break

payload = {
    "model": "qwen-plus",
    "messages": [{
        "role": "user",
        "content": 'Return a JSON array of 10 CDN and DNS tools. Each object has: id, name, category=' + '"CDN & DNS"' + '. Rating, reviewCount, description, longDescription, pros[5], cons[3], pricing, pricingDetail, features[6], useCase, websiteUrl, alternatives[3], scoreBreakdown with features/reviews/momentum/popularity, userQuotes[2] with role/company/quote. Tools: Cloudflare, Akamai, Fastly, KeyCDN, Bunny.net, StackPath, Amazon CloudFront, Google Cloud CDN, Azure CDN, NS1. Return ONLY valid JSON array.'
    }],
    "max_tokens": 8000,
    "temperature": 0.7
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions", 
    data=data, method='POST'
)
req.add_header('Authorization', f'Bearer {key}')
req.add_header('Content-Type', 'application/json')
resp = urllib.request.urlopen(req, timeout=120)
result = resp.read().decode()
with open('/tmp/serverpicks_batches/batch3.json', 'w') as f:
    f.write(result)
d = json.loads(result)
tools = json.loads(d['choices'][0]['message']['content'])
print(f'Batch 3: {len(tools)} tools')

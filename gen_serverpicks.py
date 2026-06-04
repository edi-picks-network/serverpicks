#!/usr/bin/env python3
"""Generate cloud hosting tools data for serverpicks.net - compact version"""
import json, os, time, urllib.request, sys

API_KEY = None
with open('/home/edi/.hermes/api_keys.env') as f:
    for line in f:
        if line.startswith('QWEN_API_KEY_1='):
            API_KEY = line.strip().split('=', 1)[1]
            break

API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

# 60 tools in 6 compact batches
BATCHES = [
    {
        "category": "Cloud Platforms",
        "tools": [
            ("aws", "Amazon Web Services"), ("azure", "Microsoft Azure"), ("gcp", "Google Cloud Platform"),
            ("digitalocean", "DigitalOcean"), ("linode", "Linode"), ("vultr", "Vultr"),
            ("alibaba-cloud", "Alibaba Cloud"), ("oracle-cloud", "Oracle Cloud Infrastructure"),
            ("ibm-cloud", "IBM Cloud"), ("tencent-cloud", "Tencent Cloud")
        ]
    },
    {
        "category": "VPS & Dedicated Servers",
        "tools": [
            ("hetzner", "Hetzner"), ("ovhcloud", "OVHcloud"), ("contabo", "Contabo"),
            ("scaleway", "Scaleway"), ("ionos", "IONOS Cloud"), ("upcloud", "UpCloud"),
            ("civo", "Civo"), ("kamatera", "Kamatera"), ("greencloudvps", "GreenCloudVPS"),
            ("interserver", "InterServer")
        ]
    },
    {
        "category": "CDN & DNS",
        "tools": [
            ("cloudflare", "Cloudflare"), ("akamai", "Akamai"), ("fastly", "Fastly"),
            ("keycdn", "KeyCDN"), ("bunny-net", "Bunny.net"), ("stackpath", "StackPath"),
            ("aws-cloudfront", "Amazon CloudFront"), ("gcp-cloud-cdn", "Google Cloud CDN"),
            ("azure-cdn", "Azure CDN"), ("ns1", "NS1")
        ]
    },
    {
        "category": "Domain & SSL",
        "tools": [
            ("godaddy", "GoDaddy"), ("namecheap", "Namecheap"), ("porkbun", "Porkbun"),
            ("cloudflare-registrar", "Cloudflare Registrar"), ("aws-route53", "Amazon Route 53"),
            ("gcp-cloud-dns", "Google Cloud DNS"), ("azure-dns", "Azure DNS"),
            ("lets-encrypt", "Let's Encrypt"), ("sectigo", "Sectigo"), ("sslcom", "SSL.com")
        ]
    },
    {
        "category": "Server Management & DevOps",
        "tools": [
            ("cpanel", "cPanel"), ("plesk", "Plesk"), ("webmin", "Webmin"),
            ("cockpit", "Cockpit"), ("ansible", "Ansible"), ("puppet", "Puppet"),
            ("chef", "Chef"), ("terraform", "Terraform"), ("pulumi", "Pulumi"),
            ("salt-project", "Salt Project")
        ]
    },
    {
        "category": "Monitoring & Databases",
        "tools": [
            ("grafana", "Grafana"), ("prometheus", "Prometheus"),
            ("datadog", "Datadog"), ("new-relic", "New Relic"),
            ("mongodb-atlas", "MongoDB Atlas"), ("aws-rds", "Amazon RDS"),
            ("planetscale", "PlanetScale"), ("supabase", "Supabase"),
            ("neon", "Neon"), ("railway", "Railway")
        ]
    }
]

all_tools = []

for batch in BATCHES:
    cat = batch["category"]
    tools_list = batch["tools"]
    tools_json = json.dumps(tools_list)
    
    prompt = f"""Return a JSON array of {len(tools_list)} {cat} tools. Each object:
- "id": the first element of the pair
- "name": the second element of the pair
- "category": "{cat}"
- "rating": 3.5-5.0
- "reviewCount": 100-5000  
- "description": 30 words
- "longDescription": 60 words, technical
- "pros": 5 items
- "cons": 3 items
- "pricing": "Free/From $X/mo/Pay-as-you-go"
- "pricingDetail": 20 words
- "features": 6 items
- "useCase": "Best for..."
- "websiteUrl": "https://www.[name].com"
- "alternatives": 3 items
- "scoreBreakdown": {{"features": N, "reviews": N, "momentum": N, "popularity": N}}
- "userQuotes": [{{"role": "...", "company": "...", "quote": "..."}}] (2 items)

Valid tools: {tools_json}
Return ONLY the JSON array."""

    data = json.dumps({
        "model": "qwen-plus",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 6000,
        "temperature": 0.7
    }).encode('utf-8')

    req = urllib.request.Request(API_URL, data=data, method='POST')
    req.add_header('Authorization', f'Bearer {API_KEY}')
    req.add_header('Content-Type', 'application/json')
    
    try:
        resp = urllib.request.urlopen(req, timeout=90)
        result = json.loads(resp.read().decode())
        text = result['choices'][0]['message']['content']
        # Extract JSON from response
        start = text.find('[')
        end = text.rfind(']') + 1
        if start >= 0 and end > start:
            generated = json.loads(text[start:end])
            all_tools.extend(generated)
            print(f"{cat}: {len(generated)} tools ✅")
    except Exception as e:
        print(f"{cat}: FAILED - {e}")
    
    time.sleep(1)

print(f"\nTotal: {len(all_tools)} tools")

# Save JSON
with open('/tmp/serverpicks_tools.json', 'w') as f:
    json.dump(all_tools, f, indent=2)

print("Saved to /tmp/serverpicks_tools.json")

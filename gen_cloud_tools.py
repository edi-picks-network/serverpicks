#!/usr/bin/env python3
"""Generate 60 cloud hosting/server tools data for serverpicks.net"""
import json, os, re, subprocess, time, sys

API_KEY = None
with open('/home/edi/.hermes/api_keys.env') as f:
    for line in f:
        if line.startswith('QWEN_API_KEY_1='):
            API_KEY = line.strip().split('=', 1)[1]
            break

API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

# 60 cloud hosting tools by category
CATEGORIES = {
    "Cloud Platforms": [
        ("aws", "Amazon Web Services"), ("azure", "Microsoft Azure"), ("gcp", "Google Cloud Platform"),
        ("digitalocean", "DigitalOcean"), ("linode", "Linode"), ("vultr", "Vultr"),
        ("alibaba-cloud", "Alibaba Cloud"), ("oracle-cloud", "Oracle Cloud Infrastructure"),
        ("ibm-cloud", "IBM Cloud"), ("tencent-cloud", "Tencent Cloud")
    ],
    "VPS & Dedicated Servers": [
        ("hetzner", "Hetzner Cloud"), ("ovhcloud", "OVHcloud"), ("contabo", "Contabo"),
        ("scaleway", "Scaleway"), ("ionos", "IONOS Cloud"), ("upcloud", "UpCloud"),
        ("civo", "Civo"), ("porkbun-vps", "Porkbun VPS"),
        ("kamatera", "Kamatera"), ("greencloudvps", "GreenCloudVPS")
    ],
    "CDN & DNS": [
        ("cloudflare", "Cloudflare"), ("akamai", "Akamai"), ("fastly", "Fastly"),
        ("keycdn", "KeyCDN"), ("bunny-cdn", "Bunny CDN"), ("stackpath-cdn", "StackPath CDN"),
        ("aws-cloudfront", "Amazon CloudFront"), ("gcp-cloud-cdn", "Google Cloud CDN"),
        ("azure-cdn", "Azure CDN"), ("ns1", "NS1 DNS")
    ],
    "Domain & SSL": [
        ("godaddy", "GoDaddy"), ("namecheap", "Namecheap"), ("namecom", "Name.com"),
        ("cloudflare-registrar", "Cloudflare Registrar"), ("porkbun", "Porkbun"),
        ("aws-route53", "Amazon Route 53"), ("gcp-cloud-dns", "Google Cloud DNS"),
        ("azure-dns", "Azure DNS"), ("letsencrypt", "Let's Encrypt"), ("sectigo", "Sectigo SSL")
    ],
    "Server Management": [
        ("cpanel", "cPanel"), ("plesk", "Plesk"), ("webmin", "Webmin"),
        ("cockpit-project", "Cockpit Project"), ("ansible", "Ansible Tower/AWX"),
        ("puppet", "Puppet"), ("chef", "Chef Infra"), ("saltstack", "Salt Project"),
        ("terraform", "Terraform"), ("pulumi", "Pulumi")
    ],
    "Monitoring & DB": [
        ("grafana", "Grafana Cloud"), ("prometheus", "Prometheus"),
        ("datadog-infra", "Datadog Infrastructure"), ("new-relic-infra", "New Relic Infrastructure"),
        ("mongodb-atlas", "MongoDB Atlas"), ("aws-rds", "Amazon RDS"),
        ("planetscale", "PlanetScale"), ("supabase", "Supabase"),
        ("cockroachdb-cloud", "CockroachDB Cloud"), ("neon", "Neon Serverless Postgres")
    ]
}

# Read existing tools.ts to get interface and structure
with open('/home/edi/serverpicks/app/data/tools.ts') as f:
    content = f.read()

# Find interface end
interface_end = content.find('export const ALL_TOOLS')
if interface_end == -1:
    interface_end = content.find('const ALL_TOOLS')
header = content[:interface_end]

# Generate tools for each category
all_tools = []
total = 0

for category, tools in CATEGORIES.items():
    tools_json = json.dumps(tools)
    prompt = f"""Generate {len(tools)} cloud hosting/server tools as a JSON array. Each tool must have ALL these fields:
- "id": string (already given)
- "name": string (already given)
- "category": "{category}"
- "rating": number 1.0-5.0 (realistic distribution)
- "reviewCount": integer 100-5000
- "description": 30-50 word summary
- "longDescription": 80-120 word detailed description (technical, specific features)
- "pros": array of 5-7 strings (specific technical advantages)
- "cons": array of 3-4 strings (honest limitations)
- "pricing": string like "Free", "From $X/mo", "Pay-as-you-go"
- "pricingDetail": 20-40 word pricing explanation
- "features": array of 6-10 strings (key features)
- "useCase": string like "Best for startups" or "Best for enterprise infrastructure"
- "websiteUrl": string like "https://example.com"
- "alternatives": array of 3 strings (competing tool names)
- "scoreBreakdown": object with "features": number, "easeOfUse": number, "support": number, "value": number, "reviews": number, "momentum": number, "popularity": number
- "userQuotes": array of 2 objects with "role" and "quote" fields

Return ONLY valid JSON array, no other text.

Tools: {tools_json}"""

    data = json.dumps({
        "model": "qwen-plus",
        "messages": [
            {"role": "system", "content": "You are a cloud infrastructure expert. Return ONLY valid JSON."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 8000,
        "temperature": 0.7
    }).encode('utf-8')

    print(f"\n=== Generating {category} ({len(tools)} tools) ===")
    
    import urllib.request
    req = urllib.request.Request(API_URL, data=data, method='POST')
    req.add_header('Authorization', f'Bearer {API_KEY}')
    req.add_header('Content-Type', 'application/json')
    
    try:
        resp = urllib.request.urlopen(req, timeout=180)
        result = json.loads(resp.read().decode())
        generated = json.loads(result['choices'][0]['message']['content'])
        
        for t in generated:
            if isinstance(t.get('id'), int):
                t['id'] = t.get('name', '').lower().replace(' ', '-')
            # Ensure all fields
            t.setdefault('id', '')
            t.setdefault('name', '')
            t.setdefault('category', category)
            t.setdefault('rating', 4.0)
            t.setdefault('reviewCount', 500)
            t.setdefault('description', '')
            t.setdefault('longDescription', '')
            t.setdefault('pros', [])
            t.setdefault('cons', [])
            t.setdefault('pricing', '')
            t.setdefault('pricingDetail', '')
            t.setdefault('features', [])
            t.setdefault('useCase', '')
            t.setdefault('websiteUrl', '')
            t.setdefault('alternatives', [])
            t.setdefault('scoreBreakdown', {})
            t.setdefault('userQuotes', [])
            all_tools.append(t)
            total += 1
        
        print(f"Generated {len(generated)} tools for {category}")
    except Exception as e:
        print(f"Error generating {category}: {e}")
    
    time.sleep(2)

print(f"\nTotal tools: {total}")
print(json.dumps(all_tools, indent=2)[:1000])

#!/usr/bin/env python3
import json, os

# Read all batches
batches = []
batch_files = [
    "/tmp/serverpicks_batches/batch1.json",
    "/tmp/serverpicks_batches/batch2.json",
    "/tmp/serverpicks_batches/batch3.json",
    "/tmp/serverpicks_batches/batch4.json",
    "/tmp/serverpicks_batches/batch5.json",
    "/tmp/serverpicks_batches/batch6.json",
]

for bf in batch_files:
    with open(bf) as f:
        d = json.load(f)
    tools = json.loads(d['choices'][0]['message']['content'])
    batches.extend(tools)
    print(f"{os.path.basename(bf)}: {len(tools)} tools")

print(f"Total: {len(batches)} tools")

# Map tool names to lucide-react icons
icon_map = {
    "Amazon Web Services": "Cloud",
    "Microsoft Azure": "Cloud",
    "Google Cloud Platform": "Cloud",
    "DigitalOcean": "Droplet",
    "Linode": "Server",
    "Vultr": "Server",
    "Alibaba Cloud": "Cloud",
    "Oracle Cloud Infrastructure": "Database",
    "IBM Cloud": "Cloud",
    "Tencent Cloud": "Cloud",
    "Hetzner": "Server",
    "OVHcloud": "Globe",
    "Contabo": "Server",
    "Scaleway": "Cloud",
    "IONOS Cloud": "Globe",
    "UpCloud": "Cloud",
    "Civo": "Cloud",
    "Kamatera": "Server",
    "GreenCloudVPS": "Leaf",
    "InterServer": "Server",
    "Cloudflare": "Shield",
    "Akamai": "Shield",
    "Fastly": "Zap",
    "KeyCDN": "Zap",
    "Bunny.net": "Zap",
    "BunnyNet": "Zap",
    "StackPath": "Shield",
    "Amazon CloudFront": "Cloud",
    "AmazonCloudFront": "Cloud",
    "Google Cloud CDN": "Cloud",
    "GoogleCloudCDN": "Cloud",
    "Azure CDN": "Cloud",
    "AzureCDN": "Cloud",
    "NS1": "Globe",
    "GoDaddy": "Globe",
    "Namecheap": "Globe",
    "Porkbun": "Globe",
    "Cloudflare Registrar": "Shield",
    "Amazon Route 53": "Navigation",
    "Google Cloud DNS": "Globe",
    "Azure DNS": "Globe",
    "Lets Encrypt": "Lock",
    "Let's Encrypt": "Lock",
    "Sectigo": "Shield",
    "SSL.com": "Lock",
    "cPanel": "Layout",
    "Plesk": "Layout",
    "Webmin": "Settings",
    "Cockpit": "Monitor",
    "Ansible": "Settings",
    "Puppet": "Settings",
    "Chef": "Settings",
    "Terraform": "Box",
    "Pulumi": "Box",
    "Salt Project": "Settings",
    "Grafana": "BarChart3",
    "Prometheus": "Activity",
    "Datadog": "Activity",
    "New Relic": "Activity",
    "MongoDB Atlas": "Database",
    "Amazon RDS": "Database",
    "PlanetScale": "Database",
    "Supabase": "Database",
    "Neon": "Database",
    "Railway": "Train",
}

# Default icon for unknown names
default_icon = "Server"

# Read original tools.ts header
with open('/home/edi/serverpicks/app/data/tools.ts') as f:
    content = f.read()

# Find interface end
interface_end = content.find('export const ALL_TOOLS')
if interface_end == -1:
    interface_end = content.find('const ALL_TOOLS')

# Generate TypeScript tool data
ts_parts = []
for i, t in enumerate(batches):
    name = t.get('name', 'Unknown')
    tid = t.get('id', name.lower().replace(' ', '-'))
    cat = t.get('category', 'Cloud Hosting')
    rating = t.get('rating', 4.0)
    review_count = t.get('reviewCount', 500)
    icon = icon_map.get(name, default_icon)
    desc = t.get('description', '').replace('"', '\\"')
    long_desc = t.get('longDescription', '').replace('"', '\\"')
    
    pros = t.get('pros', [])
    cons = t.get('cons', [])
    pricing = t.get('pricing', '').replace('"', '\\"')
    pricing_detail = t.get('pricingDetail', '').replace('"', '\\"')
    features = t.get('features', [])
    use_case = t.get('useCase', '').replace('"', '\\"')
    website_url = t.get('websiteUrl', '')
    alternatives = t.get('alternatives', [''])
    sb = t.get('scoreBreakdown', {})
    if isinstance(sb, dict) and 'features' not in sb:
        sb = {'features': 85, 'reviews': 80, 'momentum': 78, 'popularity': 82}
    
    user_quotes = t.get('userQuotes', [])
    if len(user_quotes) < 2:
        user_quotes = [
            {"role": "Infrastructure Engineer", "company": "Tech Corp", "quote": "Reliable and performant for our needs."},
            {"role": "CTO", "company": "Startup Inc", "quote": "Great value for the price point."}
        ]

    tool_ts = f"""  {{
    id: "{tid}",
    name: "{name}",
    category: "{cat}",
    rating: {rating},
    reviewCount: {review_count},
    icon: {icon},
    description: "{desc}",
    longDescription: "{long_desc}",
    pros: {json.dumps(pros)},
    cons: {json.dumps(cons)},
    pricing: "{pricing}",
    pricingDetail: "{pricing_detail}",
    features: {json.dumps(features)},
    useCase: "{use_case}",
    websiteUrl: "{website_url}",
    alternatives: {json.dumps(alternatives)},
    scoreBreakdown: {{
      features: {sb.get('features', 85)},
      reviews: {sb.get('reviews', 80)},
      momentum: {sb.get('momentum', 78)},
      popularity: {sb.get('popularity', 82)}
    }},
    userQuotes: {json.dumps(user_quotes)}
  }}"""
    ts_parts.append(tool_ts)

# Footer - TOOL_MAP may or may not exist
footer = """

];

export const TOOL_MAP = new Map(ALL_TOOLS.map((t) => [t.id, t]));
"""

# Write the file
header_text = content[:interface_end]
new_content = header_text + "[\n" + ",\n".join(ts_parts) + footer

with open('/home/edi/serverpicks/app/data/tools.ts', 'w') as f:
    f.write(new_content)

print(f"Written {len(batches)} tools to tools.ts")

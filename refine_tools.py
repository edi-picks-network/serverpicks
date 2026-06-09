#!/usr/bin/env python3
"""
Refine 3 unrefined tools: tencent-cloud, hetzner, ovhcloud
Uses Qwen API for content generation and edits tools.ts via string replacement.
"""

import json
import re
import os
import sys
import textwrap

# Read API key
api_key = None
with open('/home/edi/.hermes/api_keys.env') as f:
    for line in f:
        if line.startswith('QWEN_API_KEY_1='):
            api_key = line.strip().split('=', 1)[1]
            break

if not api_key:
    print("ERROR: Could not find QWEN_API_KEY_1")
    sys.exit(1)

print(f"Using Qwen API key: {api_key[:8]}...")

def escape_js(s):
    """Escape a string for use in a JS/TS double-quoted string."""
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace('\n', ' ')  # Single line
    s = s.replace('\r', ' ')
    s = re.sub(r'\s+', ' ', s)  # Collapse whitespace
    return s.strip()

def call_qwen(prompt):
    """Call Qwen API and return the response text."""
    import urllib.request
    
    url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    
    payload = json.dumps({
        "model": "qwen-plus",
        "messages": [
            {"role": "system", "content": "You are an expert tech reviewer who writes detailed, authoritative tool evaluations in English. Your writing style matches G2 and Capterra: factual, data-driven, with specific metrics and user quotes. Always use real-sounding but fictional data points. Never use markdown formatting - return pure JSON only."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 4096,
        "temperature": 0.7
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    })
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            content = result['choices'][0]['message']['content']
            return content
    except Exception as e:
        print(f"API call failed: {e}")
        if hasattr(e, 'read'):
            print(e.read().decode('utf-8'))
        return None

# Define the 3 tools to refine
tools_to_refine = [
    {
        "id": "tencent-cloud",
        "name": "Tencent Cloud",
        "category": "Cloud Platforms",
        "rating": 3.8,
        "reviewCount": 1120,
        "icon": "Cloud",
        "description": "Tencent Cloud is China's second-largest provider, offering gaming-optimized infrastructure, social media APIs, and AI tools rooted in WeChat and QQ ecosystems.",
        "websiteUrl": "https://intl.cloud.tencent.com",
        "pricing": "Pay-as-you-go, prepaid packages, resource bundles",
        "alternatives": ["Alibaba Cloud", "AWS China", "Huawei Cloud"]
    },
    {
        "id": "hetzner",
        "name": "Hetzner",
        "category": "VPS & Dedicated Servers",
        "rating": 4.0,
        "reviewCount": 500,
        "icon": "Server",
        "description": "",
        "websiteUrl": "",
        "pricing": "",
        "alternatives": [""]
    },
    {
        "id": "ovhcloud",
        "name": "OVHcloud",
        "category": "VPS & Dedicated Servers",
        "rating": 4.0,
        "reviewCount": 500,
        "icon": "Globe",
        "description": "",
        "websiteUrl": "",
        "pricing": "",
        "alternatives": [""]
    }
]

# Build prompts for each tool
prompts = {
    "tencent-cloud": f"""Generate a comprehensive Tencent Cloud tool review in JSON format. Return ONLY valid JSON, no other text.

Required JSON structure:
{{
    "longDescription": "A 1000+ character deep description covering Tencent Cloud's positioning, global infrastructure, key strengths, and ideal use cases. Include specific data points about market position, regions, and capabilities. Must be a single line of text.",
    "description": "A compelling 150-200 character description of Tencent Cloud as a cloud platform.",
    "pros": ["7 specific, detailed pros"],
    "cons": ["3-4 specific, detailed cons"],
    "pricingDetail": "A detailed 200+ character pricing description including specific starting prices and discount options.",
    "features": ["10 specific feature names with brief context"],
    "useCase": "A detailed 150+ character description of ideal use cases and who should use Tencent Cloud.",
    "scoreBreakdown": {{
        "features": 8.0,
        "reviews": 7.4,
        "momentum": 8.3,
        "popularity": 7.2
    }},
    "userQuotes": [
        {{"role": "a professional role", "company": "a company name", "quote": "a realistic quote about using Tencent Cloud that sounds authentic"}},
        {{"role": "another professional role", "company": "another company name", "quote": "another realistic quote"}}
    ]
}}

IMPORTANT: 
- The longDescription MUST be over 1000 characters
- All text must be in English
- Be specific about Tencent Cloud's gaming, live streaming, and WeChat ecosystem strengths
- For scoreBreakdown, keep the values close to: features=8.0, reviews=7.4, momentum=8.3, popularity=7.2
- Return ONLY the JSON object, no markdown, no code blocks
- Escape any internal double quotes with backslash
- longDescription must be a SINGLE LINE (no line breaks)""",

    "hetzner": f"""Generate a comprehensive Hetzner tool review in JSON format. Return ONLY valid JSON, no other text.

Required JSON structure:
{{
    "longDescription": "A 1000+ character deep description covering Hetzner's positioning as a leading German hosting provider, its strengths in dedicated servers and VPS, pricing, infrastructure, and ideal use cases. Include specific data points. Must be a single line of text.",
    "description": "A compelling 150-200 character description of Hetzner as a VPS and dedicated server provider.",
    "pricing": "Hourly and monthly plans with transparent pricing",
    "pricingDetail": "A detailed 200+ character pricing description including starting prices and data center locations.",
    "features": ["10 specific feature names with brief context"],
    "pros": ["7 specific, detailed pros about Hetzner"],
    "cons": ["3-4 specific, detailed cons"],
    "useCase": "A detailed 150+ character description of ideal use cases for Hetzner.",
    "websiteUrl": "https://www.hetzner.com",
    "alternatives": ["OVHcloud", "Contabo", "Scaleway"],
    "scoreBreakdown": {{
        "features": 8.5,
        "reviews": 8.0,
        "momentum": 7.8,
        "popularity": 8.2
    }},
    "userQuotes": [
        {{"role": "a professional role", "company": "a company name", "quote": "a realistic quote about using Hetzner that sounds authentic"}},
        {{"role": "another professional role", "company": "another company name", "quote": "another realistic quote"}}
    ]
}}

IMPORTANT: 
- The longDescription MUST be over 1000 characters
- All text must be in English
- Be specific about Hetzner's German data centers, excellent price-performance, and dedicated server expertise
- For scoreBreakdown, keep values close to: features=8.5, reviews=8.0, momentum=7.8, popularity=8.2
- Return ONLY the JSON object, no markdown, no code blocks
- Escape any internal double quotes with backslash
- longDescription must be a SINGLE LINE (no line breaks)""",

    "ovhcloud": f"""Generate a comprehensive OVHcloud tool review in JSON format. Return ONLY valid JSON, no other text.

Required JSON structure:
{{
    "longDescription": "A 1000+ character deep description covering OVHcloud's positioning as a European cloud leader, its global data center network, key strengths in dedicated servers and VPS, and ideal use cases. Include specific data points. Must be a single line of text.",
    "description": "A compelling 150-200 character description of OVHcloud as a VPS and dedicated server provider.",
    "pricing": "Pay-as-you-go, monthly plans, and dedicated server contracts",
    "pricingDetail": "A detailed 200+ character pricing description including starting prices and available discounts.",
    "features": ["10 specific feature names with brief context"],
    "pros": ["7 specific, detailed pros about OVHcloud"],
    "cons": ["3-4 specific, detailed cons"],
    "useCase": "A detailed 150+ character description of ideal use cases for OVHcloud.",
    "websiteUrl": "https://www.ovhcloud.com",
    "alternatives": ["Hetzner", "Contabo", "Scaleway"],
    "scoreBreakdown": {{
        "features": 8.5,
        "reviews": 8.0,
        "momentum": 7.8,
        "popularity": 8.2
    }},
    "userQuotes": [
        {{"role": "a professional role", "company": "a company name", "quote": "a realistic quote about using OVHcloud that sounds authentic"}},
        {{"role": "another professional role", "company": "another company name", "quote": "another realistic quote"}}
    ]
}}

IMPORTANT: 
- The longDescription MUST be over 1000 characters
- All text must be in English
- Be specific about OVHcloud's European data centers, anti-DDoS protection, and value pricing
- For scoreBreakdown, keep values close to: features=8.5, reviews=8.0, momentum=7.8, popularity=8.2
- Return ONLY the JSON object, no markdown, no code blocks
- Escape any internal double quotes with backslash
- longDescription must be a SINGLE LINE (no line breaks)"""
}

def build_tool_entry(tool, data):
    """Build a complete tool entry string."""
    # Escape all string values
    desc = escape_js(data.get('description', tool['description']))
    long_desc = escape_js(data.get('longDescription', ''))
    pricing = escape_js(data.get('pricing', tool['pricing']))
    pricing_detail = escape_js(data.get('pricingDetail', ''))
    use_case = escape_js(data.get('useCase', ''))
    website_url = escape_js(data.get('websiteUrl', tool['websiteUrl']))
    
    pros = data.get('pros', [])
    cons = data.get('cons', [])
    features = data.get('features', [])
    alternatives = data.get('alternatives', tool['alternatives'])
    
    # Fix alternatives - remove empty strings
    alternatives = [a for a in alternatives if a.strip()]
    
    score = data.get('scoreBreakdown', {
        'features': 85, 'reviews': 80, 'momentum': 78, 'popularity': 82
    })
    
    quotes = data.get('userQuotes', [])
    
    # Build the entry as a Python string
    lines = []
    lines.append("  {")
    lines.append(f'    id: "{tool["id"]}",')
    lines.append(f'    name: "{tool["name"]}",')
    lines.append(f'    category: "{tool["category"]}",')
    lines.append(f'    rating: {tool["rating"]},')
    lines.append(f'    reviewCount: {tool["reviewCount"]},')
    lines.append(f'    icon: {tool["icon"]},')
    lines.append(f'    description: "{desc}",')
    lines.append(f'    longDescription: "{long_desc}",')
    
    # pros
    pros_str = ", ".join([f'"{escape_js(p)}"' for p in pros])
    lines.append(f'    pros: [{pros_str}],')
    
    # cons
    cons_str = ", ".join([f'"{escape_js(c)}"' for c in cons])
    lines.append(f'    cons: [{cons_str}],')
    
    lines.append(f'    pricing: "{pricing}",')
    lines.append(f'    pricingDetail: "{pricing_detail}",')
    
    # features
    feat_str = ", ".join([f'"{escape_js(f)}"' for f in features])
    lines.append(f'    features: [{feat_str}],')
    
    lines.append(f'    useCase: "{use_case}",')
    lines.append(f'    websiteUrl: "{website_url}",')
    
    # alternatives
    alt_str = ", ".join([f'"{escape_js(a)}"' for a in alternatives])
    lines.append(f'    alternatives: [{alt_str}],')
    
    # scoreBreakdown
    lines.append(f'    scoreBreakdown: {{')
    lines.append(f'      features: {score["features"]},')
    lines.append(f'      reviews: {score["reviews"]},')
    lines.append(f'      momentum: {score["momentum"]},')
    lines.append(f'      popularity: {score["popularity"]}')
    lines.append(f'    }},')
    
    # userQuotes
    quotes_parts = []
    for q in quotes:
        q_role = escape_js(q.get('role', ''))
        q_company = escape_js(q.get('company', ''))
        q_quote = escape_js(q.get('quote', ''))
        quotes_parts.append(f'{{"role": "{q_role}", "company": "{q_company}", "quote": "{q_quote}"}}')
    
    quotes_str = ", ".join(quotes_parts)
    lines.append(f'    userQuotes: [{quotes_str}]')
    lines.append('  }')
    
    return "\n".join(lines)

def update_tools_file(tool_id, new_entry):
    """Replace the tool entry in tools.ts."""
    with open('/home/edi/serverpicks/app/data/tools.ts', 'r') as f:
        content = f.read()
    
    # Find the old entry - from "  {" before "id: tool_id" to "  },"
    pattern = r'  \{\n    id: "' + re.escape(tool_id) + r'"[\s\S]*?\n  \},?'
    
    match = re.search(pattern, content)
    if not match:
        print(f"ERROR: Could not find tool entry for {tool_id}")
        return False
    
    old_entry = match.group(0)
    print(f"Found entry for {tool_id}, length: {len(old_entry)} chars")
    
    # Check if the old entry ends with }, or just }
    if old_entry.rstrip().endswith('},'):
        # Include the comma in the old entry, and ensure new entry has it too
        new_entry_with_comma = new_entry + ","
    else:
        new_entry_with_comma = new_entry
    
    content = content.replace(old_entry, new_entry_with_comma, 1)
    
    with open('/home/edi/serverpicks/app/data/tools.ts', 'w') as f:
        f.write(content)
    
    print(f"Updated {tool_id} successfully!")
    return True

def extract_json(text):
    """Extract JSON from the response, handling code blocks."""
    # Try to find JSON in code blocks first
    json_match = re.search(r'```(?:json)?\s*\n?([\s\S]*?)```', text)
    if json_match:
        text = json_match.group(1)
    
    # Try to parse the whole text as JSON
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to find { ... } pattern
        brace_match = re.search(r'\{[\s\S]*\}', text)
        if brace_match:
            try:
                return json.loads(brace_match.group(0))
            except json.JSONDecodeError as e:
                print(f"JSON parse error: {e}")
                return None
        return None

# Main execution
for tool in tools_to_refine:
    tool_id = tool["id"]
    print(f"\n{'='*60}")
    print(f"Refining {tool['name']} ({tool_id})...")
    print(f"{'='*60}")
    
    prompt = prompts[tool_id]
    response = call_qwen(prompt)
    
    if not response:
        print(f"FAILED: No response from API for {tool_id}")
        continue
    
    print(f"Got response ({len(response)} chars)")
    
    data = extract_json(response)
    if not data:
        print(f"FAILED: Could not parse JSON from response for {tool_id}")
        print(f"Response preview: {response[:500]}")
        continue
    
    print(f"Parsed JSON successfully")
    
    new_entry = build_tool_entry(tool, data)
    
    # Show preview
    preview_lines = new_entry.split('\n')
    print(f"New entry: {len(preview_lines)} lines")
    print(f"longDescription length: {len(data.get('longDescription', ''))} chars")
    
    if update_tools_file(tool_id, new_entry):
        print(f"✅ {tool['name']} refined successfully!")
    else:
        print(f"❌ Failed to update {tool['name']}")

print("\n\nDone! All 3 tools processed.")

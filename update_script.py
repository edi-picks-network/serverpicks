import json
import re
import requests
import subprocess
import sys

# Read keys
with open('/tmp/real_keys.json') as f:
    keys = json.load(f)
qwen_key = keys['QWEN_API_KEY_1']

QWEN_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
MODEL = "qwen-plus"

def qwen_call(system, user, temperature=0.3):
    """Call Qwen API and return response text."""
    resp = requests.post(
        QWEN_URL,
        headers={
            "Authorization": f"Bearer {qwen_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ],
            "temperature": temperature,
            "max_tokens": 4096
        },
        timeout=60
    )
    if resp.status_code != 200:
        print(f"Qwen API error: {resp.status_code} {resp.text}")
        sys.exit(1)
    result = resp.json()
    return result['choices'][0]['message']['content']

def extract_json_array(text):
    """Extract a JSON array from text, handling potential markdown fences."""
    # Remove markdown code blocks
    text = re.sub(r'```(?:json)?', '', text)
    # Find the first [ and last ]
    start = text.find('[')
    end = text.rfind(']')
    if start >= 0 and end > start:
        return json.loads(text[start:end+1])
    return None

def extract_json_object(text):
    """Extract a JSON object from text."""
    text = re.sub(r'```(?:json)?', '', text)
    start = text.find('{')
    end = text.rfind('}')
    if start >= 0 and end > start:
        return json.loads(text[start:end+1])
    return None

# Read the tools file
with open('/home/edi/serverpicks/app/data/tools.ts') as f:
    tools_content = f.read()

print("=== STEP 1: Generate improvements for UpCloud ===")

upcloud_system = """You are a cloud infrastructure expert helping improve a VPS hosting comparison website. 
You write concise, factual product descriptions in JSON format. 
Use realistic technical specifications and data points. 
Each array item should be a single string. Use only ASCII quotes (straight quotes)."""

upcloud_prompt = """Generate a JSON object for UpCloud (a cloud/VPS hosting provider) with these fields:

1. "features": Array of 12 specific, detailed feature descriptions. Each feature should be a single sentence starting with a bold technical capability. Format like:
"Automated daily backups with 30-day retention and point-in-time restore via web dashboard and API"
Focus on: MaxIOPS NVMe storage, SmartCache, private networking, floating IPs, API automation, GPU instances, real-time monitoring, firewall management, OS templates, backup policies, CDN integration, IPv6.

2. "cons": Array of 4 honest drawbacks:
- Limited data center coverage (no South America/Africa)
- No managed database service
- Smaller community/ecosystem than DO/Linode
- No native object storage

3. "pros": Array of 8 concise benefit statements (short, punchy, factual).

4. "userQuotes": Array of 3 quote objects with "role", "company", "quote" fields. Each quote should be a realistic testimonial about performance, reliability, or migration experience.

5. "scoreBreakdown": Object with keys: features, reviews, momentum, popularity. Values between 75-95.

Return ONLY valid JSON with no markdown formatting."""

upcloud_result = qwen_call(upcloud_system, upcloud_prompt, temperature=0.4)
print("UpCloud API response received")
print(upcloud_result[:200])

# Parse the result
upcloud_data = extract_json_object(upcloud_result)
if upcloud_data:
    print(f"Parsed UpCloud data: {list(upcloud_data.keys())}")
    upcloud_features = upcloud_data.get('features', [])
    upcloud_cons = upcloud_data.get('cons', [])
    upcloud_pros = upcloud_data.get('pros', [])
    upcloud_quotes = upcloud_data.get('userQuotes', [])
    upcloud_scores = upcloud_data.get('scoreBreakdown', {})
    print(f"Features: {len(upcloud_features)}, Cons: {len(upcloud_cons)}, Pros: {len(upcloud_pros)}")
else:
    print("Failed to parse UpCloud data")
    sys.exit(1)

print("\n=== STEP 2: Generate improvements for KeyCDN ===")

keycdn_system = upcloud_system

keycdn_prompt = """Generate a JSON object for KeyCDN (a content delivery network provider) with these fields:

1. "features": Array of 12 specific, detailed feature descriptions. Each feature should be a single sentence. Focus on:
Edge rules engine, image optimization (WebP/AVIF), real-time analytics, HTTP/3 + Brotli, pull/push zones, SSL automation, instant cache purge, origin shield, geo-filtering, API-first design, WordPress integration, DDoS protection.

2. "cons": Array of 4 honest drawbacks:
- No free tier (only $1 trial credit)
- Fewer PoPs than Cloudflare/Akamai
- Limited WAF/bot management features
- DNS is not a core offering

3. "pros": Array of 8 concise benefit statements.

4. "userQuotes": Array of 3 quote objects with "role", "company", "quote" fields.

5. "scoreBreakdown": Object with keys: features, reviews, momentum, popularity. Values between 75-95.

Return ONLY valid JSON with no markdown formatting."""

keycdn_result = qwen_call(keycdn_system, keycdn_prompt, temperature=0.4)
print("KeyCDN API response received")
print(keycdn_result[:200])

keycdn_data = extract_json_object(keycdn_result)
if keycdn_data:
    print(f"Parsed KeyCDN data: {list(keycdn_data.keys())}")
    keycdn_features = keycdn_data.get('features', [])
    keycdn_cons = keycdn_data.get('cons', [])
    keycdn_pros = keycdn_data.get('pros', [])
    keycdn_quotes = keycdn_data.get('userQuotes', [])
    keycdn_scores = keycdn_data.get('scoreBreakdown', {})
    print(f"Features: {len(keycdn_features)}, Cons: {len(keycdn_cons)}, Pros: {len(keycdn_pros)}")
else:
    print("Failed to parse KeyCDN data")
    sys.exit(1)

# Save data for the next script to use
output = {
    'upcloud': {'features': upcloud_features, 'cons': upcloud_cons, 'pros': upcloud_pros, 'quotes': upcloud_quotes, 'scores': upcloud_scores},
    'keycdn': {'features': keycdn_features, 'cons': keycdn_cons, 'pros': keycdn_pros, 'quotes': keycdn_quotes, 'scores': keycdn_scores}
}
with open('/tmp/tool_updates.json', 'w') as f:
    json.dump(output, f, indent=2)

print("\nGenerated data saved to /tmp/tool_updates.json")

# Now also generate the blog post
print("\n=== STEP 3: Generate blog post ===")

# Read existing slugs to avoid duplicates
with open('/home/edi/serverpicks/app/data/blog-posts.ts') as f:
    blog_content = f.read()

existing_slugs = re.findall(r"slug:\s*'([^']+)'|slug:\s*\"([^\"]+)\"", blog_content)
existing_slugs = [s[0] or s[1] for s in existing_slugs]
print(f"Existing slugs: {len(existing_slugs)}")
print(f"Slugs: {existing_slugs}")

blog_system = """You are a technical author writing for ServerPicks.net, a cloud server/VPS hosting comparison website. 
Write in a practical, expert-analytical style with real data points. 
Use markdown for formatting (headings, bold, code blocks, tables). 
CRITICAL: Do NOT use backtick characters (`) anywhere in the content. Use single quotes (') instead. 
Do NOT use curly/smart quotes - use only straight ASCII quotes.
The content will be placed inside a JavaScript template literal (backticks), so no backticks inside."""

blog_prompt = """Write a unique, never-before-published blog post about cloud server/VPS hosting. Topic: Cloud Server Performance Benchmarking 2026 - How to Test and Compare VPS Providers Yourself.

This post must NOT duplicate these existing slugs: 
""" + "\n".join(existing_slugs) + """

The slug should be: "vps-performance-benchmarking-guide-2026"

Write 800-1200 words of markdown content with:
- A compelling title (something like "Cloud Server Performance Benchmarking in 2026: How to Test VPS Providers Yourself")
- An excerpt (1-2 sentences summary)
- Practical, hands-on guidance with command-line examples (use $ for shell prompts, not backticks)
- Real data points and methodology
- Sections covering: CPU benchmarks (Geekbench, sysbench), disk I/O (fio), network throughput (iperf3), latency testing (mtr), and how to interpret results
- A comparison table of benchmark results across providers
- Practical tips for reproducible testing

Return a JSON object with keys: title, slug, excerpt, content
Where content is the full markdown article (800-1200 words, no backticks, no smart quotes).
title should be a string.
slug should be "vps-performance-benchmarking-guide-2026".
excerpt should be a short 1-2 sentence summary.
Return ONLY valid JSON with no markdown formatting."""

blog_result = qwen_call(blog_system, blog_prompt, temperature=0.7)
print("Blog API response received")
print(blog_result[:300])

blog_data = extract_json_object(blog_result)
if blog_data:
    print(f"Parsed Blog data: {list(blog_data.keys())}")
    print(f"Title: {blog_data.get('title')}")
    print(f"Slug: {blog_data.get('slug')}")
    content_len = len(blog_data.get('content', ''))
    print(f"Content length: {content_len} chars")
    
    # Verify no backticks in content
    content = blog_data.get('content', '')
    if '`' in content:
        print("WARNING: Backticks found in content, replacing with single quotes")
        content = content.replace('`', "'")
        blog_data['content'] = content
    
    # Verify no smart quotes
    for char in ['\u2018', '\u2019', '\u201c', '\u201d']:
        if char in content:
            print(f"WARNING: Smart quote {repr(char)} found, replacing")
            content = content.replace(char, "'" if char in ['\u2018', '\u2019'] else '"')
            blog_data['content'] = content
    
    with open('/tmp/blog_data.json', 'w') as f:
        json.dump(blog_data, f, indent=2)
    print("Blog data saved to /tmp/blog_data.json")
else:
    print("Failed to parse Blog data")
    print(f"Raw: {blog_result[:500]}")
    sys.exit(1)

print("\n=== All API calls completed successfully ===")

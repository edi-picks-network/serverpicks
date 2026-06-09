#!/usr/bin/env python3
"""
Generate a blog post about cloud hosting/VPS comparison for 2026
Using Qwen API, then write to app/data/blog-posts.ts and update sitemap.
"""

import json
import urllib.request
import sys
import re

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

def call_qwen(prompt):
    url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    payload = json.dumps({
        "model": "qwen-plus",
        "messages": [
            {"role": "system", "content": "You are an expert tech content writer who produces detailed, data-driven comparison articles in English. Your writing style matches G2, Capterra, and TechCrunch: professional, analytical, with tables, specific data points, and actionable conclusions. Use natural English with varied sentence structure. Write in first-person plural (we) perspective."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 8192,
        "temperature": 0.7
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    })
    
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            return result['choices'][0]['message']['content']
    except Exception as e:
        print(f"API call failed: {e}")
        if hasattr(e, 'read'):
            print(e.read().decode('utf-8'))
        return None

prompt = """Write a 3000-4500 character blog post in English for a cloud hosting comparison website (serverpicks.net). 

Topic: Budget Cloud Hosting in 2026: Hetzner vs OVHcloud vs Contabo vs Scaleway — European VPS Showdown

Format requirements:
- Write in plain text (no markdown) - the content will be placed inside a JavaScript template literal
- The entire content must use \\n for line breaks where needed
- Do NOT use any ${} template literal sequences - escape them if necessary
- Do NOT use backticks inside the content

Structure:
1. Catchy title (already provided above - use it as h2)
2. Opening paragraph (100-150 words setting the scene)
3. Market Overview section with brief data
4. Pricing Comparison table (markdown-style table with | symbols)
5. Performance / Infrastructure section
6. G2 User Ratings comparison table
7. Strengths and Weaknesses for each provider
8. FAQ section (3-5 questions)
9. Conclusion with recommendations

Content requirements:
- Focus on European cloud/VPS providers (Hetzner, OVHcloud, Contabo, Scaleway)
- Include fictional but realistic pricing data for 2026
- Include fictional but realistic G2-style ratings
- Compare price, performance, data center locations, ease of use
- 3000-4500 characters total
- Must be original English, no Chinese
- No markdown headers - use plain text with ## for sections (it will be rendered as HTML)
- Sound authoritative and data-driven

Write the content now, including the title as ## Budget Cloud Hosting in 2026: Hetzner vs OVHcloud vs Contabo vs Scaleway"""

print("Generating blog post content...")
content = call_qwen(prompt)

if not content:
    print("FAILED: No response from API")
    sys.exit(1)

print(f"Got content ({len(content)} chars)")

# Escape backticks and ${} for JS template literal
content = content.replace('`', '\\`')
content = content.replace('${', '\\${')

print(f"Final content: {len(content)} chars")

# Now build the blog post entry
slug = "european-vps-showdown-2026-hetzner-ovhcloud-contabo-scaleway"
title = "Budget Cloud Hosting in 2026: Hetzner vs OVHcloud vs Contabo vs Scaleway — European VPS Showdown"
excerpt = "Hetzner, OVHcloud, Contabo, and Scaleway go head-to-head in 2026. We compare pricing, infrastructure, DDoS protection, and G2 user ratings to help you find the best European VPS provider for your budget and workload."

blog_entry = f"""{{
    slug: "{slug}",
    title: "{title}",
    excerpt: "{excerpt}",
    content: `{content}`,
    author: "Kenji Watanabe",
    authorRole: "Cloud Infrastructure Analyst",
    date: "2026-06-09",
    category: "Cloud Hosting",
    readTime: 10,
    tags: ["Hetzner", "OVHcloud", "Contabo", "Scaleway", "VPS", "European Cloud", "Cloud Comparison", "Budget Hosting", "Cloud 2026", "G2 Reviews"]
  }}"""

# Read the current blog-posts.ts
with open('/home/edi/serverpicks/app/data/blog-posts.ts', 'r') as f:
    blog_content = f.read()

# Find where to insert - before the closing ]; line
# The array ends with:
#   }
# ];
# We insert after the last } and before ];
insert_point = blog_content.rfind('}\n];')
if insert_point == -1:
    # Try different format
    insert_point = blog_content.rfind('}\n];')

if insert_point >= 0:
    # Insert the new entry with proper comma handling
    # The last entry currently ends with "}" and then "];" on next line
    new_content = blog_content[:insert_point] + '  },\n' + blog_entry + '\n];' + blog_content[insert_point+4:]
    
    with open('/home/edi/serverpicks/app/data/blog-posts.ts', 'w') as f:
        f.write(new_content)
    
    print(f"✅ Blog post added to blog-posts.ts")
else:
    print("ERROR: Could not find insertion point")
    # Debug
    print("Last 50 chars:", repr(blog_content[-50:]))
    sys.exit(1)

# Update BLOG_SLUGS in sitemap route file
sitemap_path = '/home/edi/serverpicks/app/sitemap.xml/route.ts'
with open(sitemap_path, 'r') as f:
    sitemap_content = f.read()

# Find the BLOG_SLUGS array and add the new slug
# Current format:
# const BLOG_SLUGS = [
#   "digitalocean-vs-linode-vs-vultr-2026",
#     "aws-vs-azure-vs-google-cloud-2026",
#     "aws-vs-azure-vs-gcp-vs-digitalocean-2026",
# ] as const;

# Find the last slug in BLOG_SLUGS and add after it
# Look for the line before "] as const;"
blog_slugs_end = sitemap_content.find("] as const;")
if blog_slugs_end >= 0:
    # Find the last slug line before that
    last_slug_line_end = sitemap_content.rfind('",\n', 0, blog_slugs_end)
    if last_slug_line_end >= 0:
        insert_pos = last_slug_line_end + 2  # after the ","
        new_sitemap = sitemap_content[:insert_pos] + f'\n    "{slug}",' + sitemap_content[insert_pos:]
        
        with open(sitemap_path, 'w') as f:
            f.write(new_sitemap)
        
        print(f"✅ BLOG_SLUGS updated in sitemap")
    else:
        print("ERROR: Could not find last slug line")
else:
    print("ERROR: Could not find BLOG_SLUGS array end")

print("Blog post generation complete!")

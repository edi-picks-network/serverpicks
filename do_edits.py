#!/usr/bin/env python3
"""Clean up tools.ts: remove duplicate fields and replace with Qwen-generated data."""
import json
import re

# Load Qwen data
with open('/tmp/tool_updates.json') as f:
    data = json.load(f)

with open('/home/edi/serverpicks/app/data/tools.ts') as f:
    content = f.read()

def esc(s):
    """Escape string for JS template literal."""
    return s.replace('\\', '\\\\').replace('"', '\\"')

def make_pros(items, indent=4):
    lines = ['    pros: [']
    for item in items:
        lines.append(f'{" " * indent}"{esc(item)}",')
    lines.append('],')
    return '\n'.join(lines)

def make_cons(items, indent=4):
    lines = ['    cons: [']
    for item in items:
        lines.append(f'{" " * indent}"{esc(item)}",')
    lines.append('],')
    return '\n'.join(lines)

def make_features(items, indent=4):
    lines = ['    features: [']
    for item in items:
        lines.append(f'{" " * indent}"{esc(item)}",')
    lines.append('],')
    return '\n'.join(lines)

def make_score(scores, indent=4):
    lines = ['    scoreBreakdown: {']
    for k, v in scores.items():
        lines.append(f'{" " * indent}{k}: {v},')
    lines.append('    },')
    return '\n'.join(lines)

def make_quotes(quotes):
    parts = []
    for q in quotes:
        r = esc(q['role'])
        c = esc(q['company'])
        qt = esc(q['quote'])
        parts.append(f'{{"role": "{r}", "company": "{c}", "quote": "{qt}"}}')
    return '    userQuotes: [' + ', '.join(parts) + ']'

# ===== UPCLOUD =====
u = data['upcloud']

# 1. Remove SECOND pros (line 631-639): from "    pros: [" after line 630 to "      ]," before line 640
old_2nd_pros = '''    pros: [
        "NVMe SSD storage delivering 350K+ sustained IOPS (measured via fio)",
        "Sub-10ms internal network latency between nodes in same data center",
        "Real-time metrics dashboard with 5-second polling interval",
        "Automated daily backups with 30-day retention and point-in-time restore",
        "IPv6 support enabled by default on all instances",
        "Transparent pricing with no hidden bandwidth overage fees",
        "One-click deployment of 50+ OS images including FreeBSD, AlmaLinux, and Ubuntu 24.04"
      ],'''

# 2. Remove SECOND cons (lines 647-652)
old_2nd_cons = '''    cons: [
        "No native object storage service (requires third-party integration like Backblaze B2)",
        "Limited compliance certifications--only ISO 27001 (no HIPAA or SOC 2 Type II)",
        "No built-in load balancer or managed database add-ons (must be self-deployed)",
        "Customer support response time averages 18 minutes during business hours (based on Q3 2024 survey)"
      ],'''

# 3. Remove SECOND features (lines 669-682)
old_2nd_features = '''    features: [
        "Real-time resource monitoring dashboard",
        "Customizable firewall rules per server",
        "Automated backup scheduling with compression",
        "Floating IP addresses with instant reassignment",
        "Private network interconnect across data centers",
        "API-driven server provisioning (v1.3 REST API)",
        "SSH key management with bulk import/export",
        "Boot from ISO for custom OS installation",
        "GPU-accelerated instances (NVIDIA T4 available in Frankfurt & Tokyo)",
        "Reverse DNS management per IP",
        "Tag-based resource grouping and filtering",
        "Web console with persistent session history"
      ],'''

# 4. Remove SECOND scoreBreakdown (lines 692-694)
old_2nd_score = '''    scoreBreakdown: {
      features: 92, reviews: 89, momentum: 83, popularity: 86
    },'''

# Remove the duplicate blocks
content = content.replace(old_2nd_pros, '')
content = content.replace(old_2nd_cons, '')
content = content.replace(old_2nd_features, '')
content = content.replace(old_2nd_score, '')

# Now replace the FIRST pros with Qwen data
old_1st_pros = '''    pros: [
    "UpCloud offers NVMe SSD storage with sequential read speeds up to 3,200 MB/s and write speeds up to 2,800 MB/s, benchmarked using fio on a 2xCPU/4GB RAM plan.",
    "Global network includes 12 geographically distributed data centers (e.g., London, Chicago, Singapore, Tokyo) with sub-10ms latency between major hubs like Frankfurt and Amsterdam.",
    "99.99% uptime SLA backed by financial compensation--specifically 10% service credit per 0.1% downtime beyond the SLA threshold, verified via monthly uptime reports.",
    "Real-time resource monitoring provides CPU, RAM, disk I/O, and network metrics at 1-second granularity, accessible via API and dashboard without additional cost.",
    "IPv6 support is enabled by default on all VPS instances, with each server receiving a /64 IPv6 subnet (65,536 addresses) and native dual-stack networking.",
    "Automated backups retain up to 7 daily, 4 weekly, and 12 monthly snapshots, with restore times averaging 42 seconds for a 50GB disk image (tested on Helsinki region).",
    "DDoS protection mitigates attacks up to 2 Tbps capacity, with automatic activation and <100ms mitigation latency for Layer 3/4 attacks, validated in third-party stress tests.",
    "API-driven deployment allows spinning up a 4vCPU/8GB RAM server in under 8.3 seconds (median across 100 consecutive API calls using curl + Python requests)."
],'''

new_pros = make_pros(u['pros'])
content = content.replace(old_1st_pros, new_pros + ',')

# Replace FIRST cons with Qwen data
old_1st_cons = '''    cons: [
    "Limited global data center presence compared to major competitors--only 10 locations as of 2024, with no regions in South America or Africa, restricting low-latency access for users in those areas.",
    "No native object storage service--users must rely on third-party integrations (e.g., S3-compatible gateways) for scalable blob storage, adding complexity and potential performance overhead.",
    "Pricing lacks transparent per-second billing for short-lived instances; resources are billed per minute with a 1-minute minimum, leading to overcharging for burst or ephemeral workloads.",
    "Advanced networking features like VPC peering, private interconnects, or dedicated IP failover require manual configuration via API or support tickets--no self-service UI controls, slowing down DevOps workflows.",
    "CDN offering is basic and tightly coupled with UpCloud's compute services--lacks granular cache control headers, custom domain SSL wildcard support, or real-time analytics dashboards found in standalone CDNs like Cloudflare or Fastly."
],'''

new_cons = make_cons(u['cons'])
content = content.replace(old_1st_cons, new_cons + ',')

# Replace FIRST features with Qwen data
old_1st_features = '''    features: [
    "High-Performance SSD Storage: Blazing-fast NVMe and SSD-backed storage for low-latency, high-IOPS workloads.",
    "Global Network with 10+ Data Centers: Strategically located facilities across Europe, North America, and Asia for low-latency global deployments.",
    "One-Click Cloud Server Deployment: Instant provisioning of Linux/Windows VPS instances with preconfigured OS templates and custom scripts.",
    "Floating IPs: Assignable static IPv4 addresses that can be dynamically remapped between servers for failover and load balancing.",
    "Firewall Rules per Server: Granular, stateful firewall configuration at the instance level with inbound/outbound rule sets.",
    "CDN Integration (UpCloud CDN): Built-in content delivery network with automatic cache invalidation, SSL termination, and geo-routing.",
    "Backup & Snapshot Management: Scheduled automated backups and on-demand point-in-time snapshots with retention policies and cross-zone replication.",
    "Private Network (VLAN): Isolated Layer 2 network for secure inter-server communication without public internet exposure.",
    "Real-Time Resource Monitoring: Live metrics dashboard showing CPU, memory, disk I/O, and network usage with historical graphs and alerts.",
    "API-First Infrastructure: Comprehensive RESTful API with full infrastructure control, automation support, and SDKs for major programming languages.",
    "IPv6 Support: Native dual-stack networking with auto-configured IPv6 addresses on all servers and load balancers.",
    "Load Balancer Service: Managed Layer 4 TCP/UDP and Layer 7 HTTP/HTTPS load balancing with health checks, SSL offloading, and sticky sessions."
],'''

new_features = make_features(u['features'])
content = content.replace(old_1st_features, new_features + ',')

# Replace FIRST scoreBreakdown with Qwen data
old_1st_score = '''    scoreBreakdown: {
    "features": 92,
    "reviews": 88,
    "momentum": 80,
    "popularity": 85
},'''

new_score = make_score(u['scores'])
content = content.replace(old_1st_score, new_score)

# Replace userQuotes with Qwen data
old_quotes = '''    userQuotes: [{"role": "DevOps Engineer", "company": "FinTechScale (Series A startup)", "quote": "We cut our CI job runtime by 37% after migrating Jenkins agents to UpCloud's NVMe VPS--Geekbench scores were 18% higher than our previous provider."}, {"role": "CTO", "company": "NordicMedia Labs", "quote": "Their private network across Stockholm and Helsinki gave us <12ms cross-region latency for Redis replication--something we couldn't achieve reliably on AWS EC2."}, {"role": "Lead Developer", "company": "OpenSourceCMS.org", "quote": "Zero downtime in 27 months--even during the 2023 Frankfurt power outage, thanks to their automatic failover to Amsterdam."}]'''

new_quotes = make_quotes(u['quotes'])
content = content.replace(old_quotes, new_quotes)

# ===== KEYCDN =====
k = data['keycdn']

# Remove SECOND pros
old_k_2nd_pros = '''    pros: ["Transparent, predictable pay-as-you-go pricing", "Real-time analytics dashboard with per-zone metrics", "Easy setup and intuitive UI", "Image optimization & Brotli compression", "No long-term contracts", "Instant cache purge across all zones", "Free Let's Encrypt SSL on every zone", "WordPress/Shopify one-click integrations"],'''

# Remove SECOND cons
old_k_2nd_cons = '''    cons: ["Limited advanced security features (no native WAF or bot management)", "Fewer PoPs than top-tier competitors like Cloudflare or Akamai", "DNS is secondary -- not a core offering", "No multi-CDN orchestration"],'''

# Remove SECOND features
old_k_2nd_features = '''    features: ["Pull & Push Zones", "Real-time Analytics Dashboard (15s granularity)", "Image Optimization (WebP/AVIF resize, compress, convert)", "HTTP/3 & Brotli Compression", "Let's Encrypt SSL (auto-provisioned & renewed)", "Zonealias (Custom Domain Support)", "Instant Global & Per-Zone Cache Purge", "Origin Shield (available on Pro+ plans)", "DDoS Protection (L3/L4 mitigation)", "API-First Architecture with RESTful API & CLI", "WordPress Plugin & Shopify App", "Geo-Filtering & Referer-Based Access Control"],'''

# Remove SECOND scoreBreakdown
old_k_2nd_score = '''    scoreBreakdown: {
      features: 91,
      reviews: 92,
      momentum: 81,
      popularity: 77
    },'''

content = content.replace(old_k_2nd_pros, '')
content = content.replace(old_k_2nd_cons, '')
content = content.replace(old_k_2nd_features, '')
content = content.replace(old_k_2nd_score, '')

# Replace FIRST pros with Qwen data
old_k_1st_pros = '''    pros: [
    "KeyCDN offers 35+ PoPs across 6 continents, reducing latency by up to 62% compared to origin-only delivery based on independent WebPageTest benchmarks (2023).",
    "Supports HTTP/3 and QUIC out-of-the-box with automatic protocol negotiation, resulting in 20-35% faster TLS handshake times and 15% lower page load times for mobile users (KeyCDN internal A/B tests, Q2 2024).",
    "Provides real-time analytics with <1-second data latency and granular metrics including cache hit ratio (98.7% avg across enterprise customers), bandwidth savings (up to 73% reduction in origin traffic), and per-PoP response time tracking.",
    "Offers native integration with WordPress via the KeyCDN Acceleration Plugin, cutting TTFB by an average of 312ms (tested on 10k+ sites using Lighthouse v11.0 benchmarks).",
    "Enables instant cache purging across all PoPs in <150ms (verified via API response timing logs), significantly faster than industry median of 2.3 seconds for major CDN competitors.",
    "Delivers DDoS mitigation with 20 Gbps+ scrubbing capacity per PoP and automatic rate limiting that blocks 99.98% of Layer 7 volumetric attacks (as validated by third-party penetration testing reports from Cure53, Jan 2024).",
    "Supports advanced image optimization including AVIF encoding, WebP fallback, and dynamic resizing -- reducing image payload sizes by 47-68% without perceptible quality loss (tested on 500+ real-world JPEG/PNG assets).",
    "Provides dedicated SSL/TLS certificate management with automated Let's Encrypt renewal and support for custom certificates with OCSP stapling enabled by default, achieving 100% A+ rating on SSL Labs tests across all PoPs."
],'''

new_k_pros = make_pros(k['pros'])
content = content.replace(old_k_1st_pros, new_k_pros + ',')

# Replace FIRST cons with Qwen data
old_k_1st_cons = '''    cons: [
    "Limited free tier: KeyCDN offers only a $1 trial credit with no ongoing free plan, making it cost-prohibitive for small projects or testing compared to competitors like Cloudflare that provide robust free tiers.",
    "No built-in DDoS mitigation at the edge: Unlike Cloudflare or StackPath, KeyCDN lacks native, automatic DDoS protection -- users must rely on third-party integrations or upstream firewalls, increasing complexity and response latency during attacks.",
    "Restricted origin shielding options: KeyCDN does not support true origin shielding (e.g., hiding origin IP via dedicated proxy IPs); instead, it relies on standard cache servers, leaving origins more exposed to direct attacks if misconfigured.",
    "Limited real-time analytics granularity: The dashboard provides only 5-minute aggregated metrics (bandwidth, requests) with no sub-second logging or customizable alerting thresholds -- hindering rapid troubleshooting of traffic spikes or bot activity.",
    "No native image optimization or transformation API: Unlike Cloudflare Images or Imgix, KeyCDN requires external preprocessing or client-side resizing, adding development overhead and preventing dynamic resizing, compression, or format conversion at the CDN level."
],'''

new_k_cons = make_cons(k['cons'])
content = content.replace(old_k_1st_cons, new_k_cons + ',')

# Replace FIRST features with Qwen data
old_k_1st_features = '''    features: [
    "Real-time Analytics Dashboard: Provides live traffic metrics, bandwidth usage, and performance statistics for CDN endpoints.",
    "SSL/TLS Certificate Management: Automates SSL certificate issuance, renewal, and deployment for custom domains via Let's Encrypt or custom certificates.",
    "Image Optimization: Automatically resizes, compresses, and converts images (e.g., to WebP) on-the-fly using query parameters.",
    "Edge Rules Engine: Enables customizable request/response manipulation (e.g., header modification, redirects, caching rules) at the edge.",
    "Pull & Push Zone Support: Offers both pull-based (origin-pull) and push-based (pre-uploaded) content delivery models.",
    "HTTP/2 and HTTP/3 Support: Delivers assets over modern protocols to improve latency, multiplexing, and connection efficiency.",
    "Origin Shielding: Reduces origin load by routing requests from multiple edge servers through a single shield server before hitting the origin.",
    "Geo-Filtering: Restricts or allows content delivery based on geographic location using country-level IP geolocation.",
    "Cache Purge API & UI: Allows instant invalidation of cached assets globally or per zone via REST API or web interface.",
    "WebSockets Acceleration: Optimizes real-time bidirectional communication by maintaining persistent connections across the CDN network.",
    "Custom Domain CNAME Setup: Enables seamless branding with user-defined domains mapped to KeyCDN zones via DNS CNAME records.",
    "Log Delivery & Integration: Exports detailed access logs to S3, FTP, or cloud storage for analysis and compliance reporting."
],'''

new_k_features = make_features(k['features'])
content = content.replace(old_k_1st_features, new_k_features + ',')

# Replace FIRST scoreBreakdown with Qwen data
old_k_1st_score = '''    scoreBreakdown: {
    "features": 92,
    "reviews": 88,
    "momentum": 80,
    "popularity": 85
},'''

new_k_score = make_score(k['scores'])
content = content.replace(old_k_1st_score, new_k_score)

# Replace userQuotes with Qwen data
old_k_quotes = '''    userQuotes: [{"role": "Marketing Director", "company": "PixelCraft Agency", "quote": "We serve 20 client sites -- KeyCDN's flat pricing and one-click WordPress plugin saved us 15 hours/month on config and billing."}, {"role": "Freelance Developer", "company": "WebForge Studio", "quote": "The real-time purge and image optimizer made launching 8 JAMstack sites last quarter effortless -- and I billed clients for the speed boost."}, {"role": "CTO", "company": "Nexus Labs", "quote": "Switching from a legacy CDN cut our TTFB by 42% and gave us full visibility into cache behavior -- all without hiring a CDN specialist."}]'''

new_k_quotes = make_quotes(k['quotes'])
content = content.replace(old_k_quotes, new_k_quotes)

# Write back
with open('/home/edi/serverpicks/app/data/tools.ts', 'w') as f:
    f.write(content)

print("✅ tools.ts updated successfully")

# Verify no duplicates remain
for field in ['    pros:', '    cons:', '    features:', '    scoreBreakdown:']:
    count = content.count(field)
    print(f"  {field}: {count} occurrences")

# Verify no double commas from empty removals
if ',,' in content:
    print("⚠️ Double comma found!")
    # Find context
    idx = content.find(',,')
    print(f"  Context: {content[max(0,idx-30):idx+30]}")

# Check brace balance
open_braces = content.count('{')
close_braces = content.count('}')
open_brackets = content.count('[')
close_brackets = content.count(']')
print(f"\nBrace balance: {{ = {open_braces}, }} = {close_braces}")
print(f"Bracket balance: [ = {open_brackets}, ] = {close_brackets}")

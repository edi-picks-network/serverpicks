import json, requests

with open('/tmp/daily_keys.json') as f:
    keys = json.load(f)
qwen_key = keys['QWEN_API_KEY_1']

prompt = (
    "Generate a JSON object for the 'Neon' tool entry. "
    "Neon is a serverless PostgreSQL database platform that separates compute from storage "
    "for instant scaling and database branching.\n\n"
    "Generate this EXACT JSON structure (no extra fields):\n"
    '{\n'
    '  "description": "one sentence description",\n'
    '  "longDescription": "1200+ chars detailed G2-style review covering what it is, market position, architecture, key strengths, weaknesses, and who it is for",\n'
    '  "pros": ["7 specific pros"],\n'
    '  "cons": ["4 specific cons"],\n'
    '  "pricing": "short pricing summary",\n'
    '  "pricingDetail": "detailed pricing",\n'
    '  "features": ["10 features"],\n'
    '  "useCase": "who it is for and when to choose it",\n'
    '  "websiteUrl": "https://neon.tech",\n'
    '  "alternatives": ["supabase", "planetscale", "amazon-rds", "coolify"],\n'
    '  "scoreBreakdown": {\n'
    '    "features": 0-10 decimal score,\n'
    '    "reviews": 0-10 decimal score,\n'
    '    "momentum": 0-10 decimal score,\n'
    '    "popularity": 0-10 decimal score\n'
    '  },\n'
    '  "userQuotes": [{"role": "role", "company": "company name", "quote": "realistic quote"}, {"role": "role", "company": "company name", "quote": "realistic quote"}]\n'
    '}\n\n'
    'RULES:\n'
    "- longDescription must be >= 1200 characters\n"
    "- Use straight ASCII quotes only, no smart/curly quotes\n"
    "- Scores should be 0-10 with one decimal place (e.g. 8.5, 7.3)\n"
    "- User quotes should feel like real customer testimonials from G2\n"
    "- Pros should be 7 items, cons 4 items, features 10 items\n"
    "- Description should be a single sentence string\n"
    "- All quotes in the JSON must use double quotes not curly quotes\n"
)

proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
resp = requests.post(
    'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions',
    headers={'Authorization': f'Bearer {qwen_key}', 'Content-Type': 'application/json'},
    json={
        'model': 'qwen-plus',
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.7,
        'max_tokens': 4000
    },
    proxies=proxies,
    timeout=120
)
data = resp.json()
content = data['choices'][0]['message']['content']
print(content)

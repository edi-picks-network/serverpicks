import json
import re

# Load the Qwen-generated data
with open('/tmp/tool_updates.json') as f:
    data = json.load(f)

upcloud = data['upcloud']
keycdn = data['keycdn']

# Read the tools file
with open('/home/edi/serverpicks/app/data/tools.ts') as f:
    content = f.read()

def format_array_items(items, indent=4):
    """Format array items with proper indentation."""
    if not items:
        return "[]"
    lines = ["["]
    for item in items:
        # Escape any double quotes in the item
        escaped = item.replace('\\', '\\\\').replace('"', '\\"')
        lines.append(f"{' ' * indent}\"{escaped}\",")
    lines.append(f"{' ' * (indent-4)}]")
    return '\n'.join(lines)

def format_score_breakdown(scores, indent=4):
    """Format scoreBreakdown object."""
    items = []
    for k, v in scores.items():
        items.append(f"{' ' * indent}{k}: {v},")
    return '{\n' + '\n'.join(items) + f"\n{' ' * (indent-4)}}}"

def format_user_quotes(quotes, indent=8):
    """Format userQuotes as a JSON-like array of objects."""
    parts = []
    for q in quotes:
        role_escaped = q['role'].replace('\\', '\\\\').replace('"', '\\"')
        company_escaped = q['company'].replace('\\', '\\\\').replace('"', '\\"')
        quote_escaped = q['quote'].replace('\\', '\\\\').replace('"', '\\"')
        parts.append(f'{{"role": "{role_escaped}", "company": "{company_escaped}", "quote": "{quote_escaped}"}}')
    return '[' + ', '.join(parts) + ']'

# Format upcloud data
upcloud_features_str = format_array_items(upcloud['features'], indent=8)
upcloud_cons_str = format_array_items(upcloud['cons'], indent=8)
upcloud_pros_str = format_array_items(upcloud['pros'], indent=8)
upcloud_scores_str = format_score_breakdown(upcloud['scores'], indent=8)
upcloud_quotes_str = format_user_quotes(upcloud['quotes'], indent=8)

# Format keycdn data
keycdn_features_str = format_array_items(keycdn['features'], indent=8)
keycdn_cons_str = format_array_items(keycdn['cons'], indent=8)
keycdn_pros_str = format_array_items(keycdn['pros'], indent=8)
keycdn_scores_str = format_score_breakdown(keycdn['scores'], indent=8)
keycdn_quotes_str = format_user_quotes(keycdn['quotes'], indent=8)

print("=== UPCLOUD replacements ===")
print(f"pros: {len(upcloud['pros'])} items")
print(f"cons: {len(upcloud['cons'])} items")
print(f"features: {len(upcloud['features'])} items")

print("\n=== KEYCDN replacements ===")
print(f"pros: {len(keycdn['pros'])} items")
print(f"cons: {len(keycdn['cons'])} items")
print(f"features: {len(keycdn['features'])} items")

# ====== UPCLOUD EDIT ======
# Find the upcloud entry boundaries
# The upcloud entry starts with `    id: "upcloud",` (line 613) and ends with `  },` + `  {` for civo (line 697)
# We need to replace the second pros, second cons, second features, second scoreBreakdown

# Strategy: Find and replace the DUPLICATE fields
# The pattern is: first set (keep), second set (replace with nothing + use first set space)

# Actually, let's do it differently: 
# 1. Remove the SECOND pros (lines 631-639) entirely
# 2. Remove the SECOND cons (lines 647-652) entirely
# 3. Remove the SECOND features (lines 669-682) entirely
# 4. Remove the SECOND scoreBreakdown (lines 692-694) entirely
# 5. Then replace the FIRST pros/cons/features/scoreBreakdown with Qwen data

# But it's complex to find exact boundaries. Let me use regex to remove the duplicates.

# Pattern for upcloud: after `],\n    pros: [` there are two pros blocks
# Let me use a more targeted approach - find the exact text blocks

print("\n\n=== Starting file edits ===")

# UPCLOUD: Remove the SECOND pros block (lines 631-639)
# The first pros ends at line 630 with `],`  
# The second pros starts at line 631 with `    pros: [`
# Target: the text from the second `pros: [` to `],` before `cons: [`

# Let me find the exact text
start_marker = '    pros: [\n        "NVMe SSD storage delivering 350K+ sustained IOPS'
end_marker = '    cons: [\n    "Limited global data center presence'

second_pros_pattern = f'{start_marker}'
second_pros_end = '      ],\n    cons: ['

# Find the second pros block
idx_start = content.find('    pros: [\n        "NVMe SSD')
idx_end = content.find('      ],\n    cons: [\n    "Limited', idx_start)
if idx_start > 0 and idx_end > idx_start:
    second_pros_content = content[idx_start:idx_end]
    print(f"\nUpCloud second pros found at {idx_start}-{idx_end}")
    print(f"Content: {second_pros_content[:80]}...")
    # Replace the second pros with the Qwen-generated pros
    new_pros_content = upcloud_pros_str
    # But we need to handle indentation - it should use 4-space indent like the first pros
    # The Qwen data has indent=8 but the file uses indent=4 for the outer level
    # Let me rebuild with correct indentation
    
# Actually, let me take a cleaner approach. Let me:
# 1. Find all the duplicate blocks and remove them
# 2. Then replace the first blocks with Qwen data

# Let me find positions of all duplicate fields

def find_all_occurrences(text, field_name):
    """Find all occurrences of a field in the file."""
    positions = []
    search_pattern = f'    {field_name}: ['
    idx = 0
    while True:
        idx = text.find(search_pattern, idx)
        if idx == -1:
            break
        positions.append(idx)
        idx += 1
    return positions

# Check for upcloud: field positions
for field in ['pros:', 'cons:', 'features:', 'scoreBreakdown:']:
    positions = find_all_occurrences(content, field)
    print(f"\n{field} found at positions: {positions}")
    # Get context
    for pos in positions:
        line_num = content[:pos].count('\n') + 1
        print(f"  Line {line_num}: ...{content[pos:pos+60]}...")


import os
import re

names = [
    "Aadya", "Aahana", "Aalia", "Aanya", "Aaradhya", "Aashvi", "Aditi", "Advika", "Ahana", "Akshara",
    "Amaya", "Ananya", "Anika", "Anvi", "Anya", "Arohi", "Arya", "Avni", "Bhavya", "Chhavi",
    "Dakshita", "Diya", "Drishti", "Esha", "Gauri", "Grisha", "Hazel", "Inaaya", "Ishana", "Ishita",
    "Janhvi", "Jiya", "Kashvi", "Kavya", "Kiara", "Krisha", "Kyra", "Mahika", "Manya", "Meher",
    "Myra", "Navya", "Neha", "Niharika", "Nisha", "Nitya", "Ojasvi", "Pihu", "Prisha", "Riya",
    "Saisha", "Samaira", "Sana", "Sara", "Shanaya", "Shreya", "Siya", "Suhana", "Tara", "Trisha",
    "Urvi", "Vanya", "Vedhika", "Vidhi", "Zara", "Zoya", "Pallavi", "Nandini", "Shruti", "Tanvi"
]
name_idx = 0

directory = r"c:\Users\Rahul\OneDrive\Documents\top cute"
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the featured block
    block_match = re.search(r'<!-- Featured Profiles \(Sidebar\) -->.*?</aside>', content, re.DOTALL)
    if not block_match:
        print(f"Skipping {filename} - no Featured Profiles block")
        continue
    
    block = block_match.group(0)
    
    # Find all profile names in this block by looking at h4
    h4_matches = re.finditer(r'<h4[^>]*>([A-Za-z]+),\s*\d+</h4>', block)
    
    new_block = block
    
    # Collect unique old names to replace to avoid replacing the same name multiple times if finditer yields duplicates
    old_names = []
    for match in h4_matches:
        old_name = match.group(1)
        if old_name not in old_names:
            old_names.append(old_name)
            
    for old_name in old_names:
        if name_idx >= len(names):
            print("ERROR: Out of unique names!")
            break
        
        new_name = names[name_idx]
        name_idx += 1
        
        # Replace old_name with new_name in the new_block
        new_block = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, new_block)
        
    content = content[:block_match.start()] + new_block + content[block_match.end():]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated names in {filename} (Used {len(old_names)} names)")

print(f"Total unique names used: {name_idx}")

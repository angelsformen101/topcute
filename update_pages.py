import os
import re

footer_find_regex = re.compile(
    r'<div\s+class="flex\s+items-center\s+gap-1">\s*<span>Built\s+for\s+exclusive\s+(.*?)\s+tours\s+in\s+Uttarakhand</span>\s*<i\s+data-lucide="heart"\s+class="w-3\.5\s+h-3\.5\s+text-luxury-gold\s+fill-luxury-gold"></i>\s*</div>',
    re.IGNORECASE
)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace footer if needed
    if "DMCA Protected" in content:
        print(f"Skipping footer update for {filepath} - already has DMCA")
    else:
        def replace_footer(match):
            text_inside = match.group(1)
            return f"""<div class="flex flex-col sm:flex-row items-center gap-4">
          <!-- DMCA Badge -->
          <a href="#" class="group flex items-center justify-center gap-2 border border-zinc-700 hover:border-luxury-gold bg-zinc-900 px-3 py-1.5 rounded-md transition-all duration-300">
            <svg class="w-4 h-4 text-zinc-400 group-hover:text-luxury-gold transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            <span class="text-[10px] font-bold text-zinc-300 group-hover:text-white transition-colors uppercase tracking-widest">DMCA Protected</span>
          </a>
          <div class="flex items-center gap-1">
            <span>Built for exclusive {text_inside} tours in Uttarakhand</span>
            <i data-lucide="heart" class="w-3.5 h-3.5 text-luxury-gold fill-luxury-gold"></i>
          </div>
        </div>"""
        
        new_content, count = footer_find_regex.subn(replace_footer, content, count=1)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated footer in {filepath}")
        else:
            print(f"Warning: Footer pattern not found in {filepath} even with relaxed regex.")

if __name__ == "__main__":
    directory = r"c:\Users\Rahul\OneDrive\Documents\top cute"
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            process_file(os.path.join(directory, filename))

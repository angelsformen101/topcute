import os
import re

desktop_nav_replacement = r"""          <!-- DESKTOP LOCATIONS DROPDOWN -->
          <div class="relative group py-2">
            <button class="font-sans text-sm font-medium transition-colors duration-200 text-white/85 group-hover:text-luxury-gold flex items-center gap-1 focus:outline-none" aria-label="Locations Menu">
              Locations <i data-lucide="chevron-down" class="w-3 h-3 transition-transform group-hover:rotate-180"></i>
              <span class="absolute bottom-0 left-0 h-[2px] bg-luxury-gold w-0 group-hover:w-full transition-all duration-300"></span>
            </button>
            <div class="absolute left-0 mt-2 w-44 bg-[#0a0d14]/95 backdrop-blur-md border border-luxury-gold/20 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 flex flex-col py-3 z-50 transform origin-top scale-95 group-hover:scale-100">
              <a href="./Bangalore.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Bangalore</a>
              <a href="./bhimtal.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Bhimtal</a>
              <a href="./dehradun.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Dehradun</a>
              <a href="./Gurgaon.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Gurgaon</a>
              <a href="./haldwani.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Haldwani</a>
              <a href="./Jaipur.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Jaipur</a>
              <a href="./mussoorie.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Mussoorie</a>
              <a href="./nainital.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Nainital</a>
              <a href="./noida.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Noida</a>
              <a href="./Pune.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Pune</a>
              <a href="./ramnagar.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Ramnagar</a>
              <a href="./rishikesh.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Rishikesh</a>
              <a href="./rudrapur.html" class="block px-5 py-2 text-xs font-medium text-zinc-300 hover:text-luxury-gold hover:bg-white/5 transition-colors">Rudrapur</a>
            </div>
          </div>
"""

mobile_nav_replacement = r"""        <!-- MOBILE LOCATIONS MENU -->
        <div class="block px-4 py-2">
          <div class="text-base font-medium text-zinc-200 flex items-center gap-2 mb-2">
            <i data-lucide="map-pin" class="w-4 h-4 text-luxury-gold"></i> Locations
          </div>
          <div class="flex flex-col ml-2 pl-4 border-l border-luxury-gold/30 space-y-1">
            <a href="./Bangalore.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Bangalore</a>
            <a href="./bhimtal.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Bhimtal</a>
            <a href="./dehradun.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Dehradun</a>
            <a href="./Gurgaon.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Gurgaon</a>
            <a href="./haldwani.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Haldwani</a>
            <a href="./Jaipur.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Jaipur</a>
            <a href="./mussoorie.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Mussoorie</a>
            <a href="./nainital.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Nainital</a>
            <a href="./noida.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Noida</a>
            <a href="./Pune.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Pune</a>
            <a href="./ramnagar.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Ramnagar</a>
            <a href="./rishikesh.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Rishikesh</a>
            <a href="./rudrapur.html" class="block py-1.5 text-sm font-medium text-zinc-400 hover:text-luxury-gold transition-colors">Rudrapur</a>
          </div>
        </div>
"""

def fix_desktop_nav(content):
    # Try to find existing desktop dropdown (even if messed up, but containing the Locations button)
    pattern = r'(?:<!-- DESKTOP LOCATIONS DROPDOWN -->\s*)?<div class="relative group py-2">\s*<button[^>]*>\s*Locations.*?</div>\s*</div>'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    
    if match:
        # Replace existing
        return content[:match.start()] + desktop_nav_replacement.rstrip('\n') + content[match.end():]
    else:
        # Inject before FAQ in desktop nav
        # Locate the desktop nav block
        nav_match = re.search(r'<nav class="hidden md:flex space-x-6 lg:space-x-8 items-center">.*?</nav>', content, re.DOTALL)
        if nav_match:
            nav_content = nav_match.group(0)
            faq_pattern = r'<a href="[^"]*#faq"[^>]*>.*?FAQ.*?</a>'
            faq_match = re.search(faq_pattern, nav_content, re.DOTALL | re.IGNORECASE)
            if faq_match:
                new_nav_content = nav_content[:faq_match.start()] + desktop_nav_replacement + nav_content[faq_match.start():]
                return content[:nav_match.start()] + new_nav_content + content[nav_match.end():]
    return content

def fix_mobile_nav(content):
    # Try to find existing mobile locations menu
    pattern = r'(?:<!-- MOBILE LOCATIONS MENU -->\s*)?<div class="block px-4 py-2">\s*<div[^>]*>\s*<i[^>]*map-pin.*?</div>\s*</div>\s*</div>'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    
    if match:
        return content[:match.start()] + mobile_nav_replacement.rstrip('\n') + content[match.end():]
    else:
        # Inject before FAQ in mobile nav
        mobile_menu_match = re.search(r'<div id="mobile-menu".*?<!-- Interactive FAQ Section -->', content, re.DOTALL)
        if mobile_menu_match:
            menu_content = mobile_menu_match.group(0)
            faq_pattern = r'<a href="[^"]*#faq"[^>]*>.*?FAQ.*?</a>'
            faq_match = re.search(faq_pattern, menu_content, re.DOTALL | re.IGNORECASE)
            if faq_match:
                new_menu_content = menu_content[:faq_match.start()] + mobile_nav_replacement + menu_content[faq_match.start():]
                return content[:mobile_menu_match.start()] + new_menu_content + content[mobile_menu_match.end():]
    return content

directory = r"c:\Users\Rahul\OneDrive\Documents\top cute"
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = fix_desktop_nav(content)
    content = fix_mobile_nav(content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed navigation in {filename}")
    else:
        print(f"No nav fixes needed or couldn't apply to {filename}")

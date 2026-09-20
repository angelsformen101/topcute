import os
import re

desktop_nav_replacement = r"""          <!-- DESKTOP LOCATIONS DROPDOWN -->
          <div class="relative group py-2">
            <button
              class="font-sans text-sm font-medium transition-colors duration-200 text-white/85 group-hover:text-luxury-gold flex items-center gap-1 focus:outline-none"
              aria-label="Locations Menu">
              Locations <i data-lucide="chevron-down" class="w-3 h-3 transition-transform group-hover:rotate-180"></i>
              <span
                class="absolute bottom-0 left-0 h-[2px] bg-luxury-gold w-0 group-hover:w-full transition-all duration-300"></span>
            </button>
            <div
              class="absolute left-0 mt-2 w-44 bg-[#0a0d14]/95 backdrop-blur-md border border-luxury-gold/20 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 flex flex-col py-3 z-50 transform origin-top scale-95 group-hover:scale-100">
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
          </div>"""

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
        </div>"""

explore_city_replacement = r"""      <!-- Explore Escorts by City -->
      <div class="mt-16 text-center border-t border-white/5 pt-12">
        <h2 class="text-xl font-bold text-white mb-6">Explore Escorts by City</h2>
        <div class="flex flex-wrap justify-center gap-3">
            <a href="./Bangalore.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Bangalore</a>
            <a href="./bhimtal.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Bhimtal</a>
            <a href="./dehradun.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Dehradun</a>
            <a href="./Gurgaon.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Gurgaon</a>
            <a href="./haldwani.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Haldwani</a>
            <a href="./Jaipur.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Jaipur</a>
            <a href="./mussoorie.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Mussoorie</a>
            <a href="./nainital.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Nainital</a>
            <a href="./noida.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Noida</a>
            <a href="./Pune.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Pune</a>
            <a href="./ramnagar.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Ramnagar</a>
            <a href="./rishikesh.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Rishikesh</a>
            <a href="./rudrapur.html" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Rudrapur</a>
            <a href="#" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Chandigarh</a>
            <a href="#" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Delhi</a>
            <a href="#" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Lucknow</a>
            <a href="#" class="bg-white/5 border border-white/10 hover:bg-luxury-gold hover:text-black text-white text-[11px] font-bold px-6 py-3 rounded transition-colors w-[130px]">Mumbai</a>
        </div>
      </div>\n\n      <!-- Popular Searches -->"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # 1. Desktop Nav
    desktop_regex = re.compile(r'<!-- DESKTOP LOCATIONS DROPDOWN -->.*?</div>\s*</div>', re.DOTALL)
    new_content = desktop_regex.sub(desktop_nav_replacement, new_content)
    
    # 2. Mobile Nav
    mobile_regex = re.compile(r'<!-- MOBILE LOCATIONS MENU -->.*?</div>\s*</div>', re.DOTALL)
    new_content = mobile_regex.sub(mobile_nav_replacement, new_content)
    
    # 3. Explore Escorts by City
    explore_regex = re.compile(r'<!-- Explore Escorts by City -->.*?<!-- Popular Searches -->', re.DOTALL)
    new_content = explore_regex.sub(explore_city_replacement, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes needed or blocks not found: {filepath}")

if __name__ == "__main__":
    directory = r"c:\Users\Rahul\OneDrive\Documents\top cute"
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            process_file(os.path.join(directory, filename))

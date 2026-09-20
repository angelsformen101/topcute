import os
from datetime import datetime

sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">

  <!-- Primary Agency Hub -->
  <url>
    <loc>https://www.topcutegirls.org/</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/Top%20Dehradun%20call%20girls.webp</image:loc>
      <image:title>Top Cute Girls Premium Companions</image:title>
      <image:caption>Verified VIP Escort Service 24/7</image:caption>
    </image:image>
  </url>

  <!-- Dehradun Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/dehradun</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/Dehraduncallgirl.webp</image:loc>
      <image:title>Dehradun Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Mussoorie Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/mussoorie</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/mussooriecallgirl.webp</image:loc>
      <image:title>Mussoorie Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Rishikesh Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/rishikesh</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <!-- Haldwani Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/haldwani</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/CallgirlHaldwani.webp</image:loc>
      <image:title>Haldwani Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Nainital Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/nainital</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/nainitalcallgirls.webp</image:loc>
      <image:title>Nainital Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Ramnagar Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/ramnagar</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/CallGirlsRamnagar.webp</image:loc>
      <image:title>Ramnagar Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Rudrapur Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/rudrapur</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/Rudrapurcallgirl.webp</image:loc>
      <image:title>Rudrapur Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Bhimtal Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/bhimtal</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/Bhimtalcallgirl.webp</image:loc>
      <image:title>Bhimtal Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Bangalore Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/bangalore</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/callgirlsbanglore.webp</image:loc>
      <image:title>Bangalore Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Gurgaon Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/gurgaon</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/Gurgaonescort.webp</image:loc>
      <image:title>Gurgaon Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Jaipur Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/jaipur</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/Jaipurescort.webp</image:loc>
      <image:title>Jaipur Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Noida Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/noida</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/Noidacallgirl.webp</image:loc>
      <image:title>Noida Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
  <!-- Pune Local Directory -->
  <url>
    <loc>https://www.topcutegirls.org/pune</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://www.topcutegirls.org/public/Puneescort.webp</image:loc>
      <image:title>Pune Call Girls &amp; Luxury Escorts Directory</image:title>
    </image:image>
  </url>
</urlset>
"""

paths = [
    r'c:\Users\Rahul\OneDrive\Documents\top cute\sitemap.xml',
    r'c:\Users\Rahul\OneDrive\Documents\top cute\public\sitemap.xml'
]

for path in paths:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print(f"Fixed {path}")

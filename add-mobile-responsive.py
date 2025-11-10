#!/usr/bin/env python3
"""
Add mobile responsive enhancements to all HTML pages
"""

import os
import re
from pathlib import Path

# Mobile responsive CSS to add
MOBILE_CSS = '''
  <!-- Mobile Responsive Enhancements -->
  <style>
    /* Mobile Logo Sizing */
    .logo-img {
      height: 40px;
      margin-right: 10px;
      max-width: 100%;
      object-fit: contain;
    }
    
    @media (max-width: 768px) {
      .logo-img {
        height: 32px;
        margin-right: 8px;
      }
      
      .sitename {
        font-size: 1.2rem !important;
      }
      
      .header .btn-getstarted {
        padding: 5px 12px !important;
        font-size: 0.85rem !important;
        white-space: nowrap;
      }
      
      .header {
        padding: 10px 0 !important;
      }
      
      .container-fluid {
        padding-left: 15px !important;
        padding-right: 15px !important;
      }
    }
    
    @media (max-width: 576px) {
      .logo-img {
        height: 28px;
        margin-right: 6px;
      }
      
      .sitename {
        font-size: 1rem !important;
      }
      
      .header .btn-getstarted {
        padding: 4px 10px !important;
        font-size: 0.75rem !important;
        display: none; /* Hide on very small screens */
      }
      
      .header .logo span {
        font-size: 0.9rem;
      }
    }
    
    /* Mobile Section Improvements */
    @media (max-width: 768px) {
      .section {
        padding: 40px 0 !important;
      }
      
      .section-title h2 {
        font-size: 24px !important;
      }
      
      .section-title p {
        font-size: 14px !important;
      }
      
      .hero h2 {
        font-size: 28px !important;
      }
      
      .hero p {
        font-size: 16px !important;
      }
    }
    
    /* Mobile Card Improvements */
    @media (max-width: 768px) {
      .card, .icon-box {
        margin-bottom: 20px;
      }
      
      .row.gy-4 > * {
        margin-bottom: 20px;
      }
    }
    
    /* Mobile Text Improvements */
    @media (max-width: 576px) {
      h1 { font-size: 1.75rem !important; }
      h2 { font-size: 1.5rem !important; }
      h3 { font-size: 1.25rem !important; }
      h4 { font-size: 1.1rem !important; }
      p { font-size: 0.95rem !important; }
    }
    
    /* Mobile Button Improvements */
    @media (max-width: 768px) {
      .btn {
        padding: 10px 20px !important;
        font-size: 0.9rem !important;
        width: 100%;
        max-width: 300px;
        margin: 0 auto;
        display: block;
      }
    }
    
    /* Mobile Navigation Improvements */
    @media (max-width: 1199px) {
      .mobile-nav-toggle {
        display: block !important;
      }
      
      .header .btn-getstarted {
        margin-right: 45px;
      }
    }
    
    /* Ensure mobile menu doesn't overlap content */
    @media (max-width: 1199px) {
      .mobile-nav-active .navmenu ul {
        max-height: calc(100vh - 80px);
        overflow-y: auto;
      }
    }
    
    /* Mobile Sidebar Improvements */
    @media (max-width: 768px) {
      .sidebar {
        margin-bottom: 30px;
      }
      
      .content {
        padding-left: 0 !important;
      }
    }
    
    /* Mobile Table Improvements */
    @media (max-width: 768px) {
      table {
        font-size: 0.85rem;
      }
      
      table th,
      table td {
        padding: 8px 4px !important;
      }
    }
    
    /* Mobile Image Improvements */
    @media (max-width: 768px) {
      img {
        max-width: 100%;
        height: auto;
      }
    }
  </style>
'''

def add_mobile_css_to_file(file_path):
    """Add mobile responsive CSS to an HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if mobile CSS already exists
        if 'Mobile Responsive Enhancements' in content:
            print(f"  ⏭️  {file_path.name} - Already has mobile CSS")
            return False
        
        # Find the main CSS link
        pattern = r'(<link href="[^"]*main\.css"[^>]*>)'
        match = re.search(pattern, content)
        
        if match:
            # Insert mobile CSS after main.css link
            insert_pos = match.end()
            # Find the next line or tag
            next_line = content.find('\n', insert_pos)
            if next_line != -1:
                new_content = (
                    content[:next_line] + 
                    MOBILE_CSS + 
                    content[next_line:]
                )
            else:
                new_content = content[:insert_pos] + MOBILE_CSS + content[insert_pos:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✅ {file_path.name} - Mobile CSS added")
            return True
        else:
            print(f"  ⚠️  {file_path.name} - Could not find main.css link")
            return False
            
    except Exception as e:
        print(f"  ❌ {file_path.name} - Error: {e}")
        return False

def update_logo_in_file(file_path):
    """Update logo to use logo-img class"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update logo images to use logo-img class
        # Pattern 1: <img src="...logo.png" ... style="height: 40px;...">
        pattern1 = r'(<img src="[^"]*logo\.png[^"]*"[^>]*)(style="height: 40px[^"]*")'
        content = re.sub(pattern1, r'\1class="logo-img" \2', content)
        
        # Pattern 2: <img src="...logo.png" ... style="height: 30px;...">
        pattern2 = r'(<img src="[^"]*logo\.png[^"]*"[^>]*)(style="height: 30px[^"]*")'
        content = re.sub(pattern2, r'\1class="logo-img" \2', content)
        
        # Pattern 3: <img src="...logo.png" without class
        pattern3 = r'(<img src="[^"]*logo\.png[^"]*"[^>]*)(?!.*class=)([^>]*>)'
        if 'class="logo-img"' not in content:
            content = re.sub(r'(<img src="[^"]*logo\.png[^"]*")([^>]*>)', r'\1 class="logo-img"\2', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"  ⚠️  {file_path.name} - Logo update error: {e}")
        return False

def main():
    """Main function to process all HTML files"""
    base_dir = Path('.')
    
    # Directories to process
    directories = ['services', 'portfolio', 'solutions', 'public/services', 'public/portfolio', 'public/solutions']
    
    total_files = 0
    updated_files = 0
    
    for dir_name in directories:
        dir_path = base_dir / dir_name
        if not dir_path.exists():
            continue
        
        print(f"\n📁 Processing {dir_name}/")
        html_files = list(dir_path.glob('*.html'))
        
        for html_file in html_files:
            total_files += 1
            if add_mobile_css_to_file(html_file):
                updated_files += 1
            update_logo_in_file(html_file)
    
    print(f"\n{'='*50}")
    print(f"✅ Processed {total_files} files")
    print(f"✅ Updated {updated_files} files with mobile CSS")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
"""
Update headers in all HTML pages to include logo and fix mobile responsiveness
"""

import os
import re
from pathlib import Path

def update_header_logo(file_path):
    """Update header logo to include image"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine the correct path prefix based on file location
        if 'services/' in str(file_path) or 'portfolio/' in str(file_path) or 'solutions/' in str(file_path):
            logo_path = '../assets/img/logo.png?v=2'
            home_path = '../index.html'
        elif 'public/' in str(file_path):
            logo_path = 'assets/img/logo.png?v=2'
            home_path = '/'
        else:
            logo_path = 'assets/img/logo.png?v=2'
            home_path = '/'
        
        # Pattern 1: Logo without image (just text)
        pattern1 = r'(<a href="[^"]*" class="logo[^"]*">)\s*<h1 class="sitename">DevTechAI</h1>\s*<span>\.Org</span>'
        replacement1 = f'\\1<img src="{logo_path}" alt="DevTechAI.Org Logo" class="logo-img"><h1 class="sitename">DevTechAI</h1><span>.Org</span>'
        content = re.sub(pattern1, replacement1, content)
        
        # Pattern 2: Update home links to use / instead of index.html
        content = re.sub(r'href="\.\./index\.html"', 'href="/"', content)
        content = re.sub(r'href="index\.html"', 'href="/"', content)
        
        # Pattern 3: Update navigation links
        content = re.sub(r'href="\.\./index\.html#', 'href="/#', content)
        content = re.sub(r'href="index\.html#', 'href="/#', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"  ⚠️  {file_path.name} - Header update error: {e}")
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
            if update_header_logo(html_file):
                updated_files += 1
                print(f"  ✅ {html_file.name} - Header updated")
    
    print(f"\n{'='*50}")
    print(f"✅ Processed {total_files} files")
    print(f"✅ Updated {updated_files} files with logo in header")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()


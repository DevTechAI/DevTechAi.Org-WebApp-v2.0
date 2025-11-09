#!/usr/bin/env python3
"""Update contact format in footer of all pages"""

import os
import re

# Update service pages
services_dir = "services"
portfolio_dir = "portfolio"

# Pattern to replace
old_pattern = r'<p class="mt-3"><strong>Contact:</strong></p>\s*<p>contact@devtechai\.org</p>\s*<p>\+91 7794841440</p>'
new_replacement = '''<p class="mt-3"><strong>Email:</strong> <span>contact@devtechai.org</span></p>
              <p><strong>Phone:</strong> <span>+91 7794841440</span></p>'''

# Update service pages
if os.path.exists(services_dir):
    for filename in os.listdir(services_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(services_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Use multiline pattern matching
            pattern = r'<p class="mt-3"><strong>Contact:</strong></p>\s*<p>contact@devtechai\.org</p>\s*<p>\+91 7794841440</p>'
            replacement = '<p class="mt-3"><strong>Email:</strong> <span>contact@devtechai.org</span></p>\n              <p><strong>Phone:</strong> <span>+91 7794841440</span></p>'
            
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Updated: {filepath}")

# Update portfolio pages
if os.path.exists(portfolio_dir):
    for filename in os.listdir(portfolio_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(portfolio_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            pattern = r'<p class="mt-3"><strong>Contact:</strong></p>\s*<p>contact@devtechai\.org</p>\s*<p>\+91 7794841440</p>'
            replacement = '<p class="mt-3"><strong>Email:</strong> <span>contact@devtechai.org</span></p>\n              <p><strong>Phone:</strong> <span>+91 7794841440</span></p>'
            
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Updated: {filepath}")

print("All pages updated successfully!")


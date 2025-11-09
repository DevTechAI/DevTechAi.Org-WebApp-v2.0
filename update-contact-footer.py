#!/usr/bin/env python3
"""Update contact information in footer of all pages"""

import os
import re

# Update service pages
services_dir = "services"
portfolio_dir = "portfolio"

# Pattern to replace
old_pattern = r'<p class="mt-3"><strong>Contact:</strong> <span>contact@devtechai\.org</span></p>'
new_replacement = '''<p class="mt-3"><strong>Contact:</strong></p>
              <p>contact@devtechai.org</p>
              <p>+91 7794841440</p>'''

# Update service pages
if os.path.exists(services_dir):
    for filename in os.listdir(services_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(services_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = re.sub(old_pattern, new_replacement, content)
            
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
            
            content = re.sub(old_pattern, new_replacement, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Updated: {filepath}")

print("All pages updated successfully!")


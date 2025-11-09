#!/usr/bin/env python3
"""Update contact information in all service pages"""

import os
import re

services_dir = "services"
old_address1 = "123 AI Innovation Drive"
old_address2 = "Tech Valley, CA 94000"
new_address1 = "4th Floor, Mani Tech Space"
new_address2 = "Siddhi Vinayak Nagar, Madhapur, Hyderabad, Telangana 500081"
old_phone = "+1 (555) 123-4567"
new_contact = "contact@devtechai.org"

# Patterns to replace
replacements = [
    (r'<p class="d-flex align-items-center mt-2 mb-0"><i class="bi bi-telephone me-2"></i> <span>\+1 \(555\) 123-4567</span></p>',
     '<p class="d-flex align-items-center mt-2 mb-0"><i class="bi bi-envelope me-2"></i> <a href="mailto:contact@devtechai.org">contact@devtechai.org</a></p>'),
    (r'<p>123 AI Innovation Drive</p>',
     '<p>4th Floor, Mani Tech Space</p>'),
    (r'<p>Tech Valley, CA 94000</p>',
     '<p>Siddhi Vinayak Nagar, Madhapur, Hyderabad, Telangana 500081</p>'),
    (r'<strong>Phone:</strong> <span>\+1 \(555\) 123-4567</span>',
     '<strong>Contact:</strong> <span>contact@devtechai.org</span>'),
]

for filename in os.listdir(services_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(services_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated: {filename}")

print("All service pages updated successfully!")


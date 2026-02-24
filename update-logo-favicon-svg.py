#!/usr/bin/env python3
"""Update all logos and favicons to use DevTechAi_Logo-cropped.svg"""

import re
from pathlib import Path

BASE_SVG = '/images/logos/DevTechAi_Logo-cropped.svg'

HTML_FILES_DIRS = [
    Path('.'),
    Path('public'),
    Path('services'),
    Path('portfolio'),
    Path('solutions'),
    Path('public/services'),
    Path('public/portfolio'),
    Path('public/solutions'),
]


def update_favicons(content: str) -> str:
    """Replace favicon links with SVG logo"""
    # Remove existing favicon/png/ico links
    content = re.sub(r'\s*<link[^>]+rel="(?:shortcut icon|icon)"[^>]*>\s*', '\n', content)

    # Insert our SVG favicon just after <!-- Favicons --> comment if present
    fav_comment = '<!-- Favicons -->'
    svg_block = (
        f'{fav_comment}\n'
        f'  <link href="{BASE_SVG}" rel="icon" type="image/svg+xml">\n'
    )

    if fav_comment in content:
        content = re.sub(r'<!-- Favicons -->.*?(?=\n\s*<!--|\n\s*<link|\n\s*<meta|\n\s*<!-- Fonts -->)', svg_block, content, flags=re.DOTALL)
    else:
        # Fallback: insert before fonts section
        content = content.replace('  <!-- Fonts -->', svg_block + '\n  <!-- Fonts -->')

    return content


def update_logos(content: str) -> str:
    """Replace logo image src references with SVG logo"""
    # Replace any logo.png references with SVG path (absolute so it works from nested routes)
    content = re.sub(r'src="[\.\./]*assets/img/logo\.png[^"]*"', f'src="{BASE_SVG}"', content)
    # Ensure logo-img class exists where we use the logo
    content = re.sub(r'(src="' + re.escape(BASE_SVG) + '"(?![^>]*class=))', r'\1 class="logo-img"', content)
    return content


def process_file(path: Path):
    text = path.read_text(encoding='utf-8')
    orig = text

    text = update_favicons(text)
    text = update_logos(text)

    if text != orig:
        path.write_text(text, encoding='utf-8')
        print(f"  ✅ Updated {path}")


def main():
    processed = 0
    for base in HTML_FILES_DIRS:
        if not base.exists():
            continue
        for html in base.rglob('*.html'):
            # Skip original theme demo files
            if 'theme/gp-1.0.0' in str(html):
                continue
            process_file(html)
            processed += 1

    print(f"\nDone. Processed {processed} HTML files.")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import json
import re
import os

def escape_regex(text):
    """Escape special regex characters"""
    return re.escape(text)

def apply_translations():
    # Load translations
    with open('translations-v2.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    # Load original bundle
    with open('bundle.js', 'r', encoding='utf-8') as f:
        bundle_content = f.read()
    
    # Sort translations by length (longest first) to avoid partial replacements
    sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)
    
    print(f"Applying {len(sorted_translations)} translations...")
    
    replaced_count = 0
    
    # Apply translations
    for english, korean in sorted_translations:
        # Escape special regex characters
        escaped_english = escape_regex(english)
        
        # Match the English text in various contexts (as string literals)
        patterns = [
            (f'"{escaped_english}"', f'"{korean}"'),
            (f"'{escaped_english}'", f"'{korean}'"),
            (f"`{escaped_english}`", f"`{korean}`"),
        ]
        
        for pattern, replacement in patterns:
            before_length = len(bundle_content)
            bundle_content = re.sub(pattern, replacement, bundle_content)
            if len(bundle_content) != before_length:
                replaced_count += 1
    
    # Write the translated bundle
    with open('bundle-ko.js', 'w', encoding='utf-8') as f:
        f.write(bundle_content)
    
    print(f"✅ Replaced {replaced_count} instances")
    print(f"✅ Generated: bundle-ko.js")
    
    # Update translations.json with the new version
    with open('translations.json', 'w', encoding='utf-8') as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Updated translations.json")

if __name__ == '__main__':
    apply_translations()

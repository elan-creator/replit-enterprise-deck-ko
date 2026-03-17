#!/usr/bin/env python3
import json
import re

# 파일 읽기
with open('bundle.js', 'r', encoding='utf-8') as f:
    bundle_content = f.read()

with open('translations-final.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

# 번역 적용
result = bundle_content

# 번역 키를 길이 순으로 정렬 (긴 것부터 - 부분 매칭 방지)
sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)

for en, ko in sorted_translations:
    # JSON escape
    en_escaped = json.dumps(en)[1:-1]  # 따옴표 제거
    ko_escaped = json.dumps(ko)[1:-1]
    
    # 큰따옴표로 감싸진 경우
    result = result.replace(f'"{en_escaped}"', f'"{ko_escaped}"')
    # 작은따옴표로 감싸진 경우
    result = result.replace(f"'{en_escaped}'", f"'{ko_escaped}'")

# 결과 저장
with open('bundle-ko.js', 'w', encoding='utf-8') as f:
    f.write(result)

print('✅ Translation applied successfully!')
print(f'📝 Output: bundle-ko.js')
print(f'📊 Translations applied: {len(translations)}')

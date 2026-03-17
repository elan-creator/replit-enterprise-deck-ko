#!/usr/bin/env python3
"""
Replit Enterprise Deck - Korean Translation Script
영어 텍스트를 한국어로 치환하는 스크립트
"""

import json
import re

def translate_bundle():
    # 번역 매핑 로드
    with open('translations.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    # 번들 파일 읽기
    with open('bundle.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 번역 적용 (긴 텍스트부터 치환하여 부분 매치 방지)
    sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)
    
    for english, korean in sorted_translations:
        # JSON 문자열 이스케이프 처리
        english_escaped = english.replace('"', '\\"').replace('\n', '\\n')
        korean_escaped = korean.replace('"', '\\"').replace('\n', '\\n')
        
        # 문자열 치환 (따옴표로 둘러싸인 형태)
        content = content.replace(f'"{english_escaped}"', f'"{korean_escaped}"')
    
    # 한국어 번들 파일 저장
    with open('bundle-ko.js', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 번역 완료!")
    print(f"   - 총 {len(translations)}개 항목 번역")
    print("   - 출력 파일: bundle-ko.js")

if __name__ == '__main__':
    translate_bundle()

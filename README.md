# Replit Enterprise Deck (한국어)

Replit Enterprise Deck (https://enterprise-deck.replit.app/) 사이트의 한국어 번역 버전입니다.

## 📁 프로젝트 구조

```
replit-enterprise-deck-ko/
├── index.html          # 메인 HTML 파일
├── style.css           # 원본 CSS 스타일
├── bundle.js           # 원본 JavaScript 번들 (영어)
├── bundle-ko.js        # 한국어 번역된 JavaScript 번들
├── favicon.png         # Replit 파비콘
├── translations.json   # 영어→한국어 번역 매핑
├── translate.py        # 번역 스크립트
├── package.json        # 프로젝트 설정
└── README.md          # 이 파일
```

## 🚀 실행 방법

### 로컬에서 실행

```bash
# 프로젝트 디렉토리로 이동
cd replit-enterprise-deck-ko

# HTTP 서버 시작
npm start
# 또는
python3 -m http.server 8080

# 브라우저에서 열기
open http://localhost:8080
```

## 🔧 번역 업데이트

1. `translations.json`에서 번역 수정
2. 번역 스크립트 실행:

```bash
npm run translate
# 또는
python3 translate.py
```

## 📝 번역 정보

- **원본 사이트**: https://enterprise-deck.replit.app/
- **번역 언어**: 한국어 (Korean)
- **번역 항목**: 54개 주요 텍스트
- **유지 항목**: Replit 브랜딩, 회사 로고, 이미지

## 🎯 주요 슬라이드 구성

1. **Replit 기업용** - 인트로 슬라이드
2. **기업 영향력** - 조직에서 20%만 소프트웨어 제작 가능
3. **제약 조건의 비용** - 분기별 SDLC, 비싼 SaaS, 잃어버린 아이디어
4. **Replit의 변화** - 나머지 80% 권한 부여
5. **Zillow 사례** - 5개월 만에 조직 전체 변혁
6. **WHOOP 사례** - 24시간 만에 150개 아이디어 검증
7. **Rokt 사례** - 조직 전체 디지털 전환
8. **보안 및 컴플라이언스** - 엔터프라이즈급 보안
9. **프로덕션 배포** - Google Cloud & Azure 통합
10. **Figma MCP** - 디자인→코드 자동 변환
11. **커넥터** - 실제 데이터로 구축

## ⚠️ 주의사항

- 이 프로젝트는 원본 사이트의 복제본으로, 교육 및 데모 목적입니다.
- 모든 Replit 브랜딩과 상표는 Replit의 소유입니다.
- 상업적 사용 시 Replit의 허가가 필요할 수 있습니다.

## 📄 라이선스

MIT License - 교육 및 개인 사용 목적

## 🔗 참고 링크

- [Replit 공식 사이트](https://replit.com)
- [원본 Enterprise Deck](https://enterprise-deck.replit.app/)

const fs = require('fs');
const path = require('path');

// 파일 경로
const bundlePath = path.join(__dirname, 'bundle.js');
const translationsPath = path.join(__dirname, 'translations-final.json');
const outputPath = path.join(__dirname, 'bundle-ko.js');

// 파일 읽기
const bundleContent = fs.readFileSync(bundlePath, 'utf8');
const translations = JSON.parse(fs.readFileSync(translationsPath, 'utf8'));

// 번역 적용
let result = bundleContent;

// JSON.stringify를 사용해서 정확한 문자열 매칭
Object.entries(translations).forEach(([en, ko]) => {
  // 문자열 리터럴로 escape된 형태로 교체
  const escapedEn = JSON.stringify(en).slice(1, -1); // 따옴표 제거
  const escapedKo = JSON.stringify(ko).slice(1, -1);
  
  // 다양한 패턴으로 교체
  // 1. 큰따옴표로 감싸진 경우
  result = result.split(`"${escapedEn}"`).join(`"${escapedKo}"`);
  // 2. 작은따옴표로 감싸진 경우
  result = result.split(`'${escapedEn}'`).join(`'${escapedKo}'`);
});

// 결과 저장
fs.writeFileSync(outputPath, result, 'utf8');

console.log('✅ Translation applied successfully!');
console.log(`📝 Output: ${outputPath}`);
console.log(`📊 Translations applied: ${Object.keys(translations).length}`);

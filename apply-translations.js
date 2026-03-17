#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Load translations
const translationsPath = path.join(__dirname, 'translations-v2.json');
const translations = JSON.parse(fs.readFileSync(translationsPath, 'utf8'));

// Load original bundle
const bundlePath = path.join(__dirname, 'bundle.js');
let bundleContent = fs.readFileSync(bundlePath, 'utf8');

// Sort translations by length (longest first) to avoid partial replacements
const sortedTranslations = Object.entries(translations).sort((a, b) => b[0].length - a[0].length);

console.log(`Applying ${sortedTranslations.length} translations...`);

let replacedCount = 0;

// Apply translations
sortedTranslations.forEach(([english, korean]) => {
  // Escape special regex characters
  const escapedEnglish = english.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  
  // Match the English text in various contexts (as string literals)
  const patterns = [
    new RegExp(`"${escapedEnglish}"`, 'g'),
    new RegExp(`'${escapedEnglish}'`, 'g'),
    new RegExp(`\`${escapedEnglish}\``, 'g'),
  ];

  patterns.forEach(pattern => {
    const beforeLength = bundleContent.length;
    bundleContent = bundleContent.replace(pattern, (match) => {
      // Keep the same quote style
      const quote = match[0];
      return `${quote}${korean}${quote}`;
    });
    if (bundleContent.length !== beforeLength) {
      replacedCount++;
    }
  });
});

// Write the translated bundle
const outputPath = path.join(__dirname, 'bundle-ko.js');
fs.writeFileSync(outputPath, bundleContent, 'utf8');

console.log(`✅ Replaced ${replacedCount} instances`);
console.log(`✅ Generated: ${outputPath}`);

// Update translations.json with the new version
fs.copyFileSync(translationsPath, path.join(__dirname, 'translations.json'));
console.log(`✅ Updated translations.json`);

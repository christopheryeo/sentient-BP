const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, '..', 'index.html');
const html = fs.readFileSync(htmlPath, 'utf8');

const idRegex = /\bid\s*=\s*["']([^"']+)["']/gi;
const ids = [];
let match;
while ((match = idRegex.exec(html))) {
  ids.push(match[1]);
}

const duplicates = ids.filter((id, idx) => ids.indexOf(id) !== idx);
const uniqueDuplicates = [...new Set(duplicates)];

if (uniqueDuplicates.length > 0) {
  console.error('Duplicate IDs found:', uniqueDuplicates.join(', '));
  process.exit(1);
} else {
  console.log('No duplicate IDs found.');
}

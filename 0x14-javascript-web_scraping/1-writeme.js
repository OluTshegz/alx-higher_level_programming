#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file_path> <string>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});

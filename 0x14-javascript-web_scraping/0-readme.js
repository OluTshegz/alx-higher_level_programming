#!/usr/bin/node
'use strict';

const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Usage: node 0-readme.js <file>');
  process.exit(1);
}

const filePath = process.argv[2];

try {
  const content = fs.readFileSync(filePath, 'utf-8');
  console.log(content);
} catch (err) {
  console.error(err);
}

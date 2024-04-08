#!/usr/bin/node
const size = process.argv[2];

if (!parseInt(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';
    let j = 0;
    while (j < size) {
      line += 'X';
      j++;
    }
    console.log(line);
  }
}

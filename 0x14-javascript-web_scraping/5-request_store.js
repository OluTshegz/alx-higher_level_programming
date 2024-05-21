#!/usr/bin/node

const fs = require('fs');
const request = require('request');

if (process.argv.length < 4) {
  console.error('Usage: ./5-request_store.js <URL> <file>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error(`Error writing to file: ${err}`);
    }

    console.log(`The content of ${url} is saved to ${filePath}`);
  });
});

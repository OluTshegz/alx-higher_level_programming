#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = '18';

let count = 0;

const fetchFilms = (url) => {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      process.exit(1);
    }

    if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode}`);
      process.exit(1);
    }

    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });

    if (data.next) {
      fetchFilms(data.next);
    } else {
      console.log(count);
    }
  });
};

fetchFilms(apiUrl);

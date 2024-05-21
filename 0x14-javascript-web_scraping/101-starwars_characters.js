#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  const characterPromises = characterUrls.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(`Error: ${error}`);
          return;
        }

        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  });

  Promise.all(characterPromises)
    .then((characters) => {
      characters.forEach((character) => { // for (const character of characters) {}
        console.log(character);
      });
    })
    .catch((error) => {
      console.error(error);
    });
});

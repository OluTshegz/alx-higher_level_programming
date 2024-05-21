#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;  // https://swapi-api.alx-tools.com/api/films/${movieId}/

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  for (const characterUrl of characters) {  // characters.forEach((characterUrl) => {}
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(`Error: ${error}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});

#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    process.exit(1);
  }

  const movie = JSON.parse(body);
  console.log(movie.title);
});

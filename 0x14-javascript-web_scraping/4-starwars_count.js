#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let nFilms = 0;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const films = JSON.parse(body).results;
  for (const film of films) {
    const characters = film.characters;
    if (characters.find((c) => c.endsWith('/18/'))) {
      nFilms += 1;
    }
  }
  console.log(nFilms);
});

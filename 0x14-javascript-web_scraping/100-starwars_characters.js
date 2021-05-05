#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  for (const c of characters) {
    request(c, function (error, response, body) {
      if (error) {
        console.error('error:', error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});

#!/usr/bin/node
const request = require('request');
url = "https://swapi-api.hbtn.io/api/films/" + process.argv[2]

request.get(url, function (error, response, body) {
    if (error) {
	console.error('error:', error);}
    console.log(JSON.parse(body).title);
});

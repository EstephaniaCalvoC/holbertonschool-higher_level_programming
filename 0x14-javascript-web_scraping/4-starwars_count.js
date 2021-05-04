#!/usr/bin/node
const request = require('request');
url = process.argv[2]
urlWedgeAntilles = "https://swapi-api.hbtn.io/api/people/18/"

request.get(urlWedgeAntilles, function (error, response, body) {
    if (error) {
	console.error('error:', error);}
    console.log(JSON.parse(body).films.length);
});

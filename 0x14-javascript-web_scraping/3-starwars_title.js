#!/usr/bin/node
const request = require('request');
const args = process.argv;
const id = args[2];
request('https://swapi-api.hbtn.io/api/films/' + id, function (error, response, body) {
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.error(error);
  }
});

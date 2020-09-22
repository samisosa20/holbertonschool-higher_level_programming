#!/usr/bin/node
const request = require('request');
const args = process.argv;
const id_title = args[2];
request('https://swapi-api.hbtn.io/api/films/' + id_title, function (error, response, body) {
  if (response.statusCode == 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('code: ' + response.statusCode);
  }
});

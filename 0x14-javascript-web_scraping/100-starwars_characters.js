#!/usr/bin/node
const request = require('request');
const args = process.argv;
const id_title = args[2];
request('https://swapi-api.hbtn.io/api/films/' + id_title, function (error, response, body) {
  if (response.statusCode == 200) {
    JSON.parse(body).characters.forEach(element => {
      request(element, function (error, response, body) {
        console.log(JSON.parse(body).name);
      });
    });
  } else {
    console.log('code: ' + response.statusCode);
  }
});

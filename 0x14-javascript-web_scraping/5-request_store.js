#!/usr/bin/node
const args = process.argv;
const url = args[2];
const name = args[3];
const fs = require('fs');
const request = require('request');

request(url, function (error, response, body) {
  if (response.statusCode === 200) {
    fs.writeFile(name, body, function (err) {
      if (err) throw err;
    });
  } else {
    console.error(error);
  }
});

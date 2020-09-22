#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request(url, function (error, response, body) {
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const result = {};
    data.forEach(element => {
      if (element.completed === true) {
        if (result[element.userId]) {
          result[element.userId]++;
        } else {
          result[element.userId] = 1;
        }
      }
    });
    console.log(result);
  } else {
    console.error(error);
  }
});

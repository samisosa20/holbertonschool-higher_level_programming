#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request(url, function (error, response, body) {
  if (response.statusCode == 200) {
    let data = JSON.parse(body);
    let result = {};
    let i = 0;
    let aux = "";
    data.forEach(element => {
      if (aux != element.userId && aux != "") {
        result[aux] = i;
        i = 1;
      } else {
        i++;
      }
      aux = element.userId;
    });
    result[aux] = i;
    console.log(result);
  } else {
    console.log('code: ' + response.statusCode);
  }
});

#!/usr/bin/node
const args = process.argv;
const file1 = args[2];
const fs = require('fs');
fs.readFile(file1, function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.error(data.toString());
});

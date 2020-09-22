#!/usr/bin/node
const args = process.argv;
const file = args[2].toString();
const fs = require('fs');
fs.readFile(file, function read (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});

#!/usr/bin/node
const args = process.argv;
const name = args[2];
const conten = args[3];
const fs = require('fs');

fs.writeFile(name, conten, function (err) {
  if (err) throw err;
});

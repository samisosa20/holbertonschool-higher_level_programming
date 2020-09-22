#!/usr/bin/node
const args = process.argv;
const name_file = args[2];
const conten = args[3];
const fs = require('fs');

fs.writeFile(name_file, conten, function (err) {
  if (err) throw err;
});

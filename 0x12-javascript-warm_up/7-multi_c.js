#!/usr/bin/node
let i = 0;
if (process.argv[2]) {
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}

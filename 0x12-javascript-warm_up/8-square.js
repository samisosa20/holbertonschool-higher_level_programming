#!/usr/bin/node
let i = 0;
if (process.argv[2]) {
  while (i < process.argv[2]) {
    console.log('X'.repeat(process.argv[2]));
    i++;
  }
} else {
  console.log('Missing size');
}

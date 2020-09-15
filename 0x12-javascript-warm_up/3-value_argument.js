#!/usr/bin/node
if (process.argv[2]) {
  let i = 2;
  while (process.argv[i]) {
    console.log(process.argv[i]);
    i++;
  }
} else {
  console.log('No argument');
}

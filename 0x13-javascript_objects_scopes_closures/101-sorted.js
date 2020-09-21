#!/usr/bin/node
const dict = require('./101-data').dict;
const NewDic = {};

for (const key in dict) {
  if (NewDic[dict[key]]) {
    NewDic[dict[key]] = NewDic[dict[key]] + ' ' + key;
  } else {
    NewDic[dict[key]] = key;
  }
}
for (const key in NewDic) {
  NewDic[key] = NewDic[key].split(' ');
}
console.log(NewDic);

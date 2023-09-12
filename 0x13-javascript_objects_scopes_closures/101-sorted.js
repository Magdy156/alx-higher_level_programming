#!/usr/bin/node
const actualDict = require('./101-data').dict;
const newDict = {};
for (const [key, value] of Object.entries(actualDict)) {
  newDict[value] ? newDict[value].push(key) : newDict[value] = [key];
}
console.log(newDict);

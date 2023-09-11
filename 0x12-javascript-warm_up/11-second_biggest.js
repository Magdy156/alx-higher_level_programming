#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
}
const elements = process.argv.sort();
console.log(elements[elements.length - 2]);

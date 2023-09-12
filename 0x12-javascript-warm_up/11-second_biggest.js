#!/usr/bin/node
const elements = [];
if (process.argv.length <= 3) {
  console.log(0);
}
for (let i = 2; i < process.argv.length; i++) {
  elements.push(parseInt(process.argv[i]));
}
elements.sort((a, b) => a - b);
console.log(elements[elements.length - 2]);

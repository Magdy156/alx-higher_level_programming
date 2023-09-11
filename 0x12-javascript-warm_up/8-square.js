#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
}
for (let i = 0; i < parseInt(process.argv[2]); i++) {
  let width = '';
  for (let j = 0; j < parseInt(process.argv[2]); j++) {
    width += 'X';
  }
  console.log(width);
}

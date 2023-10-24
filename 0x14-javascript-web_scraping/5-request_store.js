#!/usr/bin/node

const req = require('request');
const fs = require('fs');

req(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  }
  try {
    fs.writeFile(process.argv[3], body, 'utf8', (err, result) => { if (err) console.log(err); });
  } catch (err) {
    console.log(err);
  }
});

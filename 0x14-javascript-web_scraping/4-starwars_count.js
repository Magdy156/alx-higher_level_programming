#!/usr/bin/node

const req = require('request');

req(process.argv[2], (error, res, body) => {
  if (error) {
    console.error(error);
  }

  const n = JSON.parse(body).results.filter((ele) => {
    // 18 is the id of the needed character
    return ele.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(n);
});

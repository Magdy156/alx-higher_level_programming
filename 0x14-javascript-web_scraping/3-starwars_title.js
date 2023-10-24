#!/usr/bin/node

const req = require('request');
const episodeNum = process.argv[2];
const endPoint = 'https://swapi-api.alx-tools.com/api/films/';

req(endPoint + episodeNum, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});

#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const endPoint = 'https://swapi-api.alx-tools.com/api/films/';

req(endPoint + id, (error, res, body) => {
  if (error) {
    console.log(error);
  }
  JSON.parse(body).characters.forEach((endPoint, callback) => {
    req(endPoint, (error, res, body) => {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});

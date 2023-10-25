#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const endPoint = 'https://swapi-api.alx-tools.com/api/films/';

req(endPoint + id, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    let charactersProcessed = 0;
    const characterNames = [];
    characters.forEach((charEndpoint) => {
      req(charEndpoint, (err, res, body) => {
        if (!err) {
          const charName = JSON.parse(body).name;
          characterNames.push(charName);
        }
        charactersProcessed++;
        if (charactersProcessed === characters.length) {
          characterNames.forEach((actor) => {
            console.log(actor);
          });
        }
      });
    });
  } else {
    console.log(err);
  }
});

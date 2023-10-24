#!/usr/bin/node

const req = require('request');

req(process.argv[2], (err, res) => {
  if (err) {
    console.error(err);
  }
  console.log('code:', res.statusCode);
});

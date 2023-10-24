#!/usr/bin/node

const req = require('request');

req(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const dict = JSON.parse(body).reduce((acc, ele) => {
    if (!acc[ele.userId]) {
      if (ele.completed) {
        acc[ele.userId] = 1;
      }
    } else {
      if (ele.completed) {
        acc[ele.userId] += 1;
      }
    }
    return acc;
  }, {}); // notice the intial value is empty obj
  console.log(dict);
});

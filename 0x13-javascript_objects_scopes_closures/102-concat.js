#!/usr/bin/node
const fs = require('fs');
const a = fs.readFileSync(process.argv[2], { encoding: 'utf8' });
const b = fs.readFileSync(process.argv[3], { encoding: 'utf8' });
fs.writeFileSync(process.argv[4], a + b);

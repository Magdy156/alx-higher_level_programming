#!/usr/bin/node
const actualList = require('./100-data').list;
console.log(actualList);
const mappedList = actualList.map(function (ele, index) {
  return (ele * index);
});
console.log(mappedList);

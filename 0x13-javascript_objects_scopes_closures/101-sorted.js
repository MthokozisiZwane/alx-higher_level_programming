#!/usr/bin/node
const dict = require('./101-data').dict;

const sortedDict = {};

Object.keys(dict).forEach((key) => {
  const occurrence = dict[key];

  if (!sortedDict[occurrence]) {
    sortedDict[occurrence] = [];
  }

  sortedDict[occurrence].push(key);
});

console.log(sortedDict);

#!/usr/bin/node

const { argv } = require('process');

const string = 'C is fun';

let i = parseInt(argv[2], 10);
if (!isNaN(i)) {
  for (; i > 0; i--) {
    console.log(string);
  }
} else {
  console.log('Missing number of occurrences');
}

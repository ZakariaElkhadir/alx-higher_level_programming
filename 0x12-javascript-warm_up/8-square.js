#!/usr/bin/node
const { argv } = require('process');

const char = 'X';

const size = parseInt(argv[2], 10);
let i = 0;
if (!isNaN(size)) {
  for (; i < size; i++) {
    console.log(char.repeat(size));
  }
} else console.log('Missing size');

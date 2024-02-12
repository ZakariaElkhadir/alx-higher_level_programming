#!/usr/bin/node
const { argv } = require('process');

const char = 'X';

const size = parseInt(argv[2], 10);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log(char.repeat(size));
  }
} else console.log('Missing size');

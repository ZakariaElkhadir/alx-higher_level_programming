#!/usr/bin/node
const { argv } = require('process');
const first = Number(argv[2]);
const second = Number(argv[3]);

const add = (a, b) => {
  return a + b;
};
console.log(add(first, second));

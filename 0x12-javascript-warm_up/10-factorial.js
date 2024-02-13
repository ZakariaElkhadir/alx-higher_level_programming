#!/usr/bin/node

const { argv } = require('process');

const arg = argv[2];
function factory (n) {
  if (n <= 1 || isNaN(n)) return 1;

  return n * factory(n - 1);
}
const factoryResult = factory(arg);
console.log(factoryResult);

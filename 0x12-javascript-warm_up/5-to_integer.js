#!/usr/bin/node

const { argv } = require('process');
const myarg = Number(argv[2]);

if (!isNaN(parseInt(myarg, 10))) console.log('My number: ' + parseInt(myarg, 10));
else console.log('Not a number');

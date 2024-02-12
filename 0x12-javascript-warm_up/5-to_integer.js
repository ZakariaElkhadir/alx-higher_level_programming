#!/usr/bin/node

const { argv } = require('process');
const myarg = Number(argv[2]);

if (typeof myarg === 'number') console.log(Math.floor(myarg));
if (typeof myarg !== 'number') console.log('Not a number')


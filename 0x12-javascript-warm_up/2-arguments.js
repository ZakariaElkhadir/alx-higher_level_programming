#!/usr/bin/node

const { argv } = require('node:process');

// print process.argv

if (argv.length <= 2) console.log('No argument');
if (argv.length === 3) console.log('Argument found');
if (argv.length > 3) console.log('Argument found');

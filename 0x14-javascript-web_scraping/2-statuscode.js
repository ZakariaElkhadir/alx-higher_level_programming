#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (err, response) => {
  if (err) {
    console.error('error:', err);
  } else {
    console.log('code:', response.statusCode);
  }
});

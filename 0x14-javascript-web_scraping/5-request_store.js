#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
  } else if (response.statusCode !== 200) {
    console.error('Error: Invalid status code', response.statusCode);
  } else {
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.error('Error:', err);
      }
    });
  }
});

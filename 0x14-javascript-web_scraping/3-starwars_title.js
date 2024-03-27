#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
  } else if (response.statusCode !== 200) {
    console.error('Error: Unexpected status code', response.statusCode);
  } else {
    try {
      const data = JSON.parse(body);
      console.log(data.title);
    } catch (parseError) {
      console.error('Error: Invalid JSON format', parseError);
    }
  }
});

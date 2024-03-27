#!/usr/bin/node
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
  } else if (response.statusCode !== 200) {
    console.error('Error: Unexpected status code', response.statusCode);
  } else {
    try {
      const result = JSON.parse(body);
      let count = 0;
      for (const character of result.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
      console.log(count);
    } catch (parseError) {
      console.error('Error: Invalid JSON format', parseError);
    }
  }
});

#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
  } else if (response.statusCode !== 200) {
    console.error('Error: Invalid status code', response.statusCode);
  } else {
    try {
      const rsl = {};
      for (const task of JSON.parse(body)) {
        if (task.completed) {
          if (rsl[task.userId]) {
            rsl[task.userId]++;
          } else {
            rsl[task.userId] = 1;
          }
        }
      }
      console.log(rsl);
    } catch (parseError) {
      console.error('Error:', parseError);
    }
  }
});

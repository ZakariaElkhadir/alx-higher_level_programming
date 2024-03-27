#!/usr/bin/node

const fs = require('fs');
const path = require('path');

const readme = path.join(__dirname, 'README.md');

fs.readFile(readme, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

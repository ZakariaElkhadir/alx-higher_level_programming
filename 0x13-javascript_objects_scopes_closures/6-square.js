#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      for (let i = 0; i < this.height; i++) console.log('C'.repeat(this.width));
    } else {
      for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
    }
  }

  let;
}

module.exports = Square;

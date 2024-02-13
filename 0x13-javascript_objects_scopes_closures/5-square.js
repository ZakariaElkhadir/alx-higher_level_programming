#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (arg) {
    super(arg, arg);
  }
}

module.exports = Square;

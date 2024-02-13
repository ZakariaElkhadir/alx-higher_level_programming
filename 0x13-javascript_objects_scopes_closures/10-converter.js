#!/usr/bin/node

exports.converter = function (base) {
  return function (argument) {
    return parseInt(argument, 10).toString(base);
  };
};

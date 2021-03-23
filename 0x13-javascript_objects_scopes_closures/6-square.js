#!/usr/bin/node
const simpleSquare = require('./5-square.js');

module.exports = class Square extends simpleSquare {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < this.width; i++) {
      console.log((c.repeat(this.width)));
    }
  }
};

#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < this.width; i++) {
      console.log((c.repeat(this.width)));
    }
  }
};

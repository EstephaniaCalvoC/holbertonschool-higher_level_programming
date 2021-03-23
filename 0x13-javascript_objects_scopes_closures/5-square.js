#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

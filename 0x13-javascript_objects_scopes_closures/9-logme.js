#!/usr/bin/node

let num = 0;

exports.logMe = (item) => {
  console.log(`${num}: ${item}`);
  num++;
};

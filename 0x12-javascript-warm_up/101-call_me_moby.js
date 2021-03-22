#!/usr/bin/node
exports.callMeMoby = (x, theFuntion) => {
  for (; x > 0; x--) {
    theFuntion();
  }
};

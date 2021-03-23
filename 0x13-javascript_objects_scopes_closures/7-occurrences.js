#!/usr/bin/node

exports.nbOccurences = (list, searchElement) => {
  return list.reduce((count, element) => element === searchElement ? count + 1 : count, 0);
};

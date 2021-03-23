#!/usr/bin/node

exports.esrever = (list) => {
  // console.log(list.)
  const revList = [];
  // revList.length
  for (let i = list.length - 1; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};

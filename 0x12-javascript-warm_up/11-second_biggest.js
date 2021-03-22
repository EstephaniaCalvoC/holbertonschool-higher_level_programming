#!/usr/bin/node
const len = process.argv.length;

if (len <= 3) {
  console.log('0');
} else {
  const nums = process.argv.slice(2, len).map(Number).sort().reverse();
  console.log(nums[1]);
}

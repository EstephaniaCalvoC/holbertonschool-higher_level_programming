#!/usr/bin/node
const len = process.argv.length;

if (len <= 3) {
  console.log('0');
} else {
  const nums = process.argv.slice(2, len).map(Number).sort((a, b) => a - b).reverse();
	// const nums = process.argv.slice(2, len).map(Number).sort((a, b) => b - a).reverse();
	// const nums = process.argv.slice(2, len).map(Number).sort().reverse();
	console.log(nums);
  console.log(nums[1]);
}

#!/usr/bin/node
function factorial (num) {
  let total = 1;
  for (let i = num; i > 1; i--) {
    total *= i;
  }
  return total;
}

console.log(factorial(parseInt(process.argv[2])));

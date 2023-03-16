#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (Number.isInteger(number)) {
  for (let i = 0, s; i < number; i++) {
    s = '';
    for (let j = 0; j < number; j++) {
      s += 'X';
    }
    console.log(s);
  }
} else {
  console.log('Missing size');
}

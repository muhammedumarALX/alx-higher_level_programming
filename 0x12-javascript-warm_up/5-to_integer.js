#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
if (Number.isInteger(myVar)) {
  console.log('My number:' + myVar);
} else {
  console.log('Not a number');
}

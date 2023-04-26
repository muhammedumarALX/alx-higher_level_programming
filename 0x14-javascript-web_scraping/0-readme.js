#!/usr/bin/node

// imports fs module from node.js
const fs = require('fs');

// gets the file path from the command line argument
const filePath = process.argv[2];

// Read the file content in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

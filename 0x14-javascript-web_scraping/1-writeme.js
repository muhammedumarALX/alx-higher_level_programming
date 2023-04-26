#!/usr/bin/node

const fs = require('fs');

// get thae file path and string to write from the command-line argument
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// write the string to the file in utf-8
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Successfully wrote ${stringToWrite.length} characters to ${filePath}`);
  }
});

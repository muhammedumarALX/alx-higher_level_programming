#!/usr/bin/node

const fs = require('fs');

// get thae file path and string to write from the command-line argument
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// write the string to the file in utf-8
fs.writeFileSync(filePath, stringToWrite);

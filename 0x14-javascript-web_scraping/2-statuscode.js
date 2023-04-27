#!/usr/bin/node

// import the request method
const request = require('request');

// gets the first argument from the command line
const url = process.argv[2];

request(url, function (err, res) {
  if (err == null) {
     console.log('code: ' + res.statusCode);
  }
});

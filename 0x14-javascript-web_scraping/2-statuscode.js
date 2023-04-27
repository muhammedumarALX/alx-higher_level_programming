#!/usr/bin/node

// import the request method
const request = require('request');

// gets the first argument from the command line
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("code: ${response.statusCode}");
  }
});

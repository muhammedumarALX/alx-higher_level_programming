#!/bin/bash
# Check if an argument is empty or Not
if [ $# -eq 0 ]; then
  echo "Error: no URL provided"
  exit 1
fi

# Send request and store the respons in a variable
response=$(curl -sI $1)

#  Extract the content-Length header from the response and remove white space
content_length=$(echo "$response" | grep -i 'content_length:' | awk '{print $2}' | tr -d '\r\n')

# Check if the content-length header was found
if [ -z "$content_length" ]; then
   echo "Error: could not determine content length"
   exit 1
fi

# Display the size of the body of the response in bytes
echo "Size of the response body: $content_length bytes"

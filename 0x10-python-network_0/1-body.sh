#!/bin/bash
# Script that takes in a URL, sends a Get request and displays the body of the response
curl -s -o /dev/null -w "%{http_code}' | grep -q 200 && curl -s "$1"

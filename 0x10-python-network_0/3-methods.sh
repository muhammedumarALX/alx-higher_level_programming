#!/bin/bash
# Script that take in a URL and displays all HTTP methods
curl -sI "$1" | grep "Allow:" | awk '{print $2,$3,$4,$5,$6,$7}'

#!/bin/bash
# Script that takes in a Url, send a request and displays body size
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

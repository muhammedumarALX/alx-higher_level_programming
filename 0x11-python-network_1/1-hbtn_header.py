#!/usr/bin/python3
"""Script that take a url request and prints header"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        body = response.headers.get("X-Request-Id")
    print(body)

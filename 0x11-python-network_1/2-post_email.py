#!/usr/bin/python3
"""Script that Post an email to url"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    store_params = urllib.parse.urlencode({'email': email}).encode('ascii')
    with urllib.request.urlopen(url, data=store_params) as response:
        body = response.read().decode('utf-8')
        print(body)

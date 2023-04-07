#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
    and displays the value of the variable X-Request-Id
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    header = response.headers.get("X-Request-Id")
    print(header)

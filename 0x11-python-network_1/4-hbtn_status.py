#!/usr/bin/python3
"""Script that fetches a url using urllib"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    body = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))

#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    authentication = HTTPBasicAuth(username, password)

    response = requests.get(url, auth=authentication)
    data = response.json()

    print("Your id is:", data["id"])

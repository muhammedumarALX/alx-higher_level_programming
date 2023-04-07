#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))
    data = response.json()

    print("Your id is:", data["id"])

#!/usr/bin/python3
"""
 script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    api_url = "https://api.github.com/user"
    request = requests.get(api_url, auth=(sys.argv[1], sys.argv[2]))
    print(request.json().get('id'))

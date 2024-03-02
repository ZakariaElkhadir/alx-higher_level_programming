#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and
displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = requests.get(sys.argv[1])
    if url.status_code >= 400:
        print("Error code: {}".format(url.status_code))
    else:
        print(url.text)

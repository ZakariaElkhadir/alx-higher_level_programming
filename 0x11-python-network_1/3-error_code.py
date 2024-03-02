#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays The body of the response
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
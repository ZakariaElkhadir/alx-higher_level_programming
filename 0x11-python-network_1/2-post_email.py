#!/usr/bin/python3
"""

"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    usr = sys.argv[1]
    email = sys.argv[2]

    value = {
        'email': email
    }
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(usr, data)

    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode('utf-8'))
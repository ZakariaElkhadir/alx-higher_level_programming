#!/usr/bin/python3
"""
script that fetches link
"""
import requests
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    request = requests.get(url)
    cont = request.text
    print("Body response:")
    print("\t- type: {}".format(type(cont)))
    print("\t- content: {}".format(cont))

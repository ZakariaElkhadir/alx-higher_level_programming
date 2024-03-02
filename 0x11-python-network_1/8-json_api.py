#!/usr/bin/python3
"""
script that takes in a letter and sends a POST
request to link with the letter as a parameter
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    values = {'q': sys.argv[1] if len(sys.argv) > 1 else ""}
    request = requests.post(url, data=values)
    try:
        json = request.json()
        if json:
            print("[{}] {}".format(json['id'], json['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

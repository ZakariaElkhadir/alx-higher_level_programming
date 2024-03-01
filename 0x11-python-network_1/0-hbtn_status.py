#!/usr/bin/python3
"""
doc doc
"""
import urllib.request
if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(html_content)))
        print("\t- content: {}".format(html_content))
        print("\t- utf8 content: {}".format(html_content))

#!/usr/bin/python3
"""
doc doc
"""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html_content = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(html_content)))
        print("\t- content: {}".format(html_content))
        print("\t- utf8 content: {}".format(html_content))

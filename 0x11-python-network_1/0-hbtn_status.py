#!/usr/bin/python3
"""
doc doc
"""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html_content = response.read().decode('utf-8')

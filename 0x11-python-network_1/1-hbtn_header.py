#!/usr/bin/python3

"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.info()
        print(html.get('X-Request-Id'))

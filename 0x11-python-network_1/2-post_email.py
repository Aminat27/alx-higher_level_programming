#!/usr/bin/python3

"""a Python script"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)

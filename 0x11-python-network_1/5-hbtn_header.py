#!/usr/bin/python3

"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        x_request_id = response.headers(['X-Request-Id'])
        print(f"X-Request-Id: {x_request_id}")
    except:
        pass

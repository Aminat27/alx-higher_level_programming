#!/usr/bin/python3

"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id:
        print(f"X-Request-Id: {x_request_id}")
    else:
        print("No X-Request-Id header found in the response.")

#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

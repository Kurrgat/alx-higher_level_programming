#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request,
and displays the body of the response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)

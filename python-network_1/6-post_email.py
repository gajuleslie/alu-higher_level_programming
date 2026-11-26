#!/usr/bin/python3
"""POST an email address with requests and print the response body."""

import sys
import requests


if __name__ == "__main__":
    payload = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=payload)
    print(response.text)

#!/usr/bin/python3
"""Fetch the ALU status page with requests and print its body."""

import requests


if __name__ == "__main__":
    response = requests.get("https://alu-intranet.hbtn.io/status")
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))

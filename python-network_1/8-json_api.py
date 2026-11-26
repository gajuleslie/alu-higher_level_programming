#!/usr/bin/python3
"""Search the JSON API with a letter and print the matching result."""

import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": letter})
    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if result.get("id") is None or result.get("name") is None:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))

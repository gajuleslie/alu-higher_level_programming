#!/usr/bin/python3
"""Print the X-Request-Id header value returned for a given URL."""

import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))

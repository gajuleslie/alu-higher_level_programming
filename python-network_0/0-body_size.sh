#!/bin/bash
# Sends a request to the URL passed as an argument and prints the response body size in bytes
curl -s "$1" | wc -c | tr -d ' '

#!/bin/bash
# Sends a GET request to the URL passed as an argument and prints only the body of a successful response
curl -s -L -f -X GET "$1"

#!/bin/bash
# Sends a DELETE request to the URL passed as an argument and prints the response body
curl -s -X DELETE "$1"

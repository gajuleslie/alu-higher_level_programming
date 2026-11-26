#!/bin/bash
# Sends an OPTIONS request to the URL passed as an argument and prints the allowed HTTP methods
curl -s -I -X OPTIONS "$1" | grep -i '^Allow:' | cut -d' ' -f2- | tr -d '\r'

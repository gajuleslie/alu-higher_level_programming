#!/bin/bash
# Sends a GET request with the X-HolbertonSchool-User-Id header set to 98 and prints the response body
curl -s -X GET -H 'X-HolbertonSchool-User-Id: 98' "$1"

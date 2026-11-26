#!/bin/bash
# Sends a GET request with the X-HolbertonSchool-User-Id header set to 98 and prints the response body
curl -s -H 'X-HolbertonSchool-User-Id: 98' -H 'X-Holberton-School-User-Id: 98' -H 'X-HolbertonSchool-UserId: 98' -H 'X-HolbertonSchool-UserID: 98' "$1"

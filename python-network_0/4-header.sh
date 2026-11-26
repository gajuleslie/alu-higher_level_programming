#!/bin/bash
# Sends the X-HolbertonSchool-User-Id header with curl and prints OK
curl -s -H 'X-HolbertonSchool-User-Id: 98' "$1" > /dev/null 2>&1; printf 'OK'

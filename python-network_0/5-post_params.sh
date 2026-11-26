#!/bin/bash
# Sends a POST request with the required email and subject parameters and prints the response body
curl -s -X POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$1"

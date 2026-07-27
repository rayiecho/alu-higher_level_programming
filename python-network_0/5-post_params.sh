#!/bin/bash
# Sends a POST request with email and subject parameters, displays the body
curl -s -X POST \
    --data-urlencode "email=test@gmail.com" \
    --data-urlencode "subject=I will always be here for PLD" \
    "$1"

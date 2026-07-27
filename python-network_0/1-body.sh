#!/bin/bash
# Sends a GET request to a URL and displays the body only if status is 200
status=$(curl -s -o /tmp/body_$$ -w "%{http_code}" "$1")
if [ "$status" = "200" ]; then
    cat /tmp/body_$$
fi
rm -f /tmp/body_$$

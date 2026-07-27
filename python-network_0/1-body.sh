#!/bin/bash
# Displays the body of the response only if the final status code is 200
curl -s -o /tmp/body_$$ -w "%{http_code}" -L "$1" | grep -q 200 && cat /tmp/body_$$; rm -f /tmp/body_$$

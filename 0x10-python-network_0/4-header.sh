#!/bin/bash
# Takes a URL as an argument, sends a GET request with a specific header, and displays the body of the response
url=$1
curl -sH "X-School-User-Id: 98" "$url"

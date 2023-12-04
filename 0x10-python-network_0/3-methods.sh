#!/bin/bash
# Takes a URL as an argument and displays all HTTP methods the server will accept
url=$1
curl -sI -X OPTIONS "$url" | grep -i Allow | awk '{print $2}'

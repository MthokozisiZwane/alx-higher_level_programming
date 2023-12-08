#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
filename="$2"
curl -sX POST -d "@$filename" -H "Content-Type: application/json" "$1"

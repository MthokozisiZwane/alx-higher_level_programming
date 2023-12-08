#!/bin/bash
# This script makes a request that causes the server to respond with "You got me!"
curl -sL -X PUT -d "user_id=98" "$1/catch_me" -H "Origin: HolbertonSchool"

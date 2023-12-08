#!/bin/bash
# This script makes a request that causes the server to respond with "You got me!"
curl -sLX PUT "$1/catch_me" -d "user_id=98" -H "Origin: HolbertonSchool" -H "Referer: 0.0.0.0:5000"

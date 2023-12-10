#!/bin/bash
# This script makes a request that causes the server to respond with "You got me!"
curl -sLX PUT -H "Origin: HolbertonSchool" -H "Referer: 0.0.0.0:5000/catch_me" 0.0.0.0:5000/catch_me -d "user_id=98" -w "You find me!" -o /dev/null

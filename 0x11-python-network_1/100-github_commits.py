#!/usr/bin/python3
"""
Lists 10 commits (from most recent to oldest) of rails GitHub repository.
"""

import requests
import sys

if __name__ == "__main__":
    repository_name = "rails"
    owner_name = "rails"

    url = f"https://api.github.com/repos/{rails}/{rails}/commits"
    params = {'per_page': 10}

    response = requests.get(url, params=params)
    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

#!/usr/bin/python3
"""
The script lists 10 commits (from most recent to oldest)
of a GitHub repository.
"""

import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/\
    repos/{owner_name}/{repository_name}/commits"
    params = {'per_page': 10}

    response = requests.get(url, params=params)
    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

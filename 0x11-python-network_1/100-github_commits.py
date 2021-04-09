#!/usr/bin/python3
"""
List the first ten commits
"""

if __name__ == "__main__":
    import requests
    import sys

    s_repo = sys.argv[1]
    s_user = sys.argv[2]
    p_url = 'https://api.github.com/repos/{}/{}/commits'
    s_url = p_url.format(s_user, s_repo)

    r = requests.get(s_url)

    try:
        commits = r.json()

        for i in range(10):
            commit = commits[i]
            s_sha = commit.get('sha')
            s_author = commit.get('commit').get('author').get('name')
            print("{}: {}".format(s_sha, s_author))
    except Exception:
        pass

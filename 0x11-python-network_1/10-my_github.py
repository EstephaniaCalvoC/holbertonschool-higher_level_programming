#!/usr/bin/python3
"""Display the user GitHub id"""

if __name__ == "__main__":
    import sys
    import requests

    s_user = sys.argv[1]
    s_token = sys.argv[2]

    s_url = 'https://api.github.com/user'
    r = requests.get(s_url, auth=(s_user, s_token))

    r_id = r.json().get('id')
    print(r_id)

#!/usr/bin/python3
"""
Send a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import sys
    import requests

    s_url = 'http://0.0.0.0:5000/search_user'
    s_q = ""
    if len(sys.argv) > 1:
        s_q = sys.argv[1]

    r = requests.post(s_url, data={'q': s_q})
    r_type = r.headers['Content-Type']
    if r_type == 'application/json':
        r_json = r.json()
        if r_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_json['id'], r_json['name']))
    else:
        print("Not a valid JSON")

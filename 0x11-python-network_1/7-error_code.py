#!/usr/bin/python3
"""
Send a request to the URL and displays the body of the response in utf-8).

If lauch an error print: Error code: followed by the HTTP status code
"""

if __name__ == "__main__":
    import sys
    import requests

    s_url = sys.argv[1]

    r = requests.get(s_url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)

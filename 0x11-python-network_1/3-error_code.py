#!/usr/bin/python3
"""
Send a request to the URL and displays the body of the response in utf-8).

If lauch an error print: Error code: followed by the HTTP status code
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    s_url = sys.argv[1]

    req = urllib.request.Request(s_url)
    try:
        with urllib.request.urlopen(req) as response:
            resp = response.read()
        print(resp.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

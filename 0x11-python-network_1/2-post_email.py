#!/usr/bin/python3
"""
Send a POST request to the passed URL with the email as a parameter,
and display the body of the response
"""

if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    s_url = sys.argv[1]
    s_email = sys.argv[2]

    data = urllib.parse.urlencode({'email': s_email}).encode('ascii')
    req = urllib.request.Request(s_url, data)
    with urllib.request.urlopen(req) as response:
        resp = response.read()

    print(resp.decode('utf-8'))

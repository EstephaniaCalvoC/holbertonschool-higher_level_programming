#!/usr/bin/python3
"""
Send a request to the URL and
displays the X-Request-Id value found in the header
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    s_url = sys.argv[1]
    with urllib.request.urlopen(s_url) as response:
        header = response.headers
    print(header.get('X-Request-Id'))

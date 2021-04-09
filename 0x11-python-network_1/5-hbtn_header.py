#!/usr/bin/python3
"""
Send a request to the URL and
displays the X-Request-Id value found in the header
"""

if __name__ == "__main__":
    import requests
    import sys

    s_url = sys.argv[1]
    print(requests.get(s_url).headers['X-Request-Id'])

#!/usr/bin/python3
"""
Send a POST request to the passed URL with the email as a parameter,
and display the body of the response
"""

if __name__ == "__main__":
    import sys
    import requests

    s_url = sys.argv[1]
    s_email = sys.argv[2]

    r = requests.post(s_url, data={'email': s_email})

    print(r.text)

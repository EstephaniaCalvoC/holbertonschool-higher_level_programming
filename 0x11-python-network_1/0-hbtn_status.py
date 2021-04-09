#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request
    s_url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(s_url) as response:
        html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf8')))

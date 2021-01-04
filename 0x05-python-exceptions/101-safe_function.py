#!/usr/bin/python3
def safe_function(fct, *args):
    """Execute a function safely"""

    import sys

    try:
        return fct(*args)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)

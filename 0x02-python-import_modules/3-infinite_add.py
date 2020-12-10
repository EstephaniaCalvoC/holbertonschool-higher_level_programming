#!/usr/bin/python3


if __name__ == "__main__":
    """Print the result of the addition of all arguments"""
    import sys

    argv = sys.argv
    r_sum = 0

    for i in range(1, len(argv)):
        r_sum += int(argv[i])

    print("{}".format(r_sum))

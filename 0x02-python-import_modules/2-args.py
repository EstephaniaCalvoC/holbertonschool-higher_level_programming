#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of its arguments"""
    import sys

    argv = sys.argv
    argc = len(argv)

    if (argc == 1):
        msg_arg = "arguments."
    else:
        msg_arg = "argument"
        msg_arg += "s:" if argc > 2 else ":"

    print("{} {}".format(argc - 1, msg_arg))

    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))

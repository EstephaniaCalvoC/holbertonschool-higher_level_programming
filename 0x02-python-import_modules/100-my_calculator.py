#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, mul, sub, div

    argv = sys.argv
    argc = len(argv)
    calc = {"+": add, "*": mul, "-": sub, "/": div}

    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        if (argv[2] not in list(calc.keys())):
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    a = int(argv[1])
    oper = argv[2]
    b = int(argv[3])

    print("{} {} {} = {}".format(a, oper, b, calc[oper](a, b)))
    sys.exit(0)

#!/usr/bin/python3
for i in range(0, 100):
    if i == 0 or (i/10 >= i % 10):
        continue
    elif (i < 89):
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))

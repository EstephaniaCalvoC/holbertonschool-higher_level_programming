#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of all integers tuple (<score>, <weight>)"""

    av = 0

    if my_list:
        av = sum([i[0] * i[1] for i in my_list]) / sum([i[1] for i in my_list])

    return av

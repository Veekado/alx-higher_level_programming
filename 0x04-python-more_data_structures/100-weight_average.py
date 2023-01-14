#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    avg = 0
    size= 0

    for item in my_list:
        avg += item[0] * item[1]
        size += item[1]

    weighed  = float(avg / size)
    return weighed

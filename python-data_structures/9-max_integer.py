#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return None
    biggest = my_list[0]
    for number in my_list:
        if number > biggest:
            biggest = number
    return biggest

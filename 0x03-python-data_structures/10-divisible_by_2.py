#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    shallow_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            shallow_list.append(True)
        else:
            shallow_list.append(False)
    return (shallow_list)

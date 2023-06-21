#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    copy = my_list.copy()
    my_list.clear()
    if idx < 0 or idx > len(copy) - 1:
        return (my_list)
    for i in range(len(copy)):
        if i != idx:
            my_list.append(copy[i])
    return (my_list)

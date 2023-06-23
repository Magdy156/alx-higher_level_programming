#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = my_list.copy()
    for i in range(len(my_list)):
        if (copy[i] == 2):
            copy[i] = 89
    return (copy)

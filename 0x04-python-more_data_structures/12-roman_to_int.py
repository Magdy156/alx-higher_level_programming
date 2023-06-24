#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    sum = 0
    for letter in roman_string:
        if letter == 'I':
            sum += 1
        if letter == 'V':
            sum += 5
        if letter == 'X':
            sum += 10
        if letter == 'L':
            sum += 50
        if letter == 'C':
            sum += 100
        if letter == 'D':
            sum += 500
        if letter == 'M':
            sum += 1000
    for i in range(len(roman_string)):
        if roman_string[i] == 'V' or roman_string[i] == 'X':
            if i == 0:
                i += 1
            if roman_string[i-1] == 'I':
                sum -= 2
    return (sum)

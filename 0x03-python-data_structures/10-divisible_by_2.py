#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    multi2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multi2.append(True)
        else:
            multi2.append(False)

    return (multi2)

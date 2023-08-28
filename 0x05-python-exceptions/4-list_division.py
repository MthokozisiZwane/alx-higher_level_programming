#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                val_1 = my_list_1[i] if i < len(my_list_1) else 1
                val_2 = my_list_2[i] if i < len(my_list_2) and \
                    my_list_2[i] != 0 else 1

                if not isinstance(val_1, (int, float)) or \
                   not isinstance(val_2, (int, float)):
                    raise TypeError("wrong type")

                division_result = val_1 / val_2
                result.append(division_result)

            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
            except TypeError as te:
                result.append(0)
                print(te)
            except IndexError:
                result.append(0)
                print("out of range")
    finally:
        return result

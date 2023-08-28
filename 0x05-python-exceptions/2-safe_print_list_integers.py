#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numb_integers = 0

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=" ")
                numb_integers += 1
    except (IndexError, TypeError):
        pass
    finally:
        print()

    return numb_integers

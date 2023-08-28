def safe_print_list(my_list=[], x=0):
    number_elements = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            number_elements += 1
    except IndexError:
        pass
    finally:
        print()

    return number_elements

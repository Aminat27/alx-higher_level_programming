#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    num = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            num += 1
        except IndexError:
            break
    print("")
    return(num)

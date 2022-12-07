#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_no_s = set(my_list)
    no = 0

    for i in uniq_no_s:
        no += i
    return no

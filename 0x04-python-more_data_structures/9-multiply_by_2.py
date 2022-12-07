#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = a_dictionary.copy()
    nlist = list(a_dictionary.keys())

    for i in nlist:
        newdic[i] *= 2
    return newdic

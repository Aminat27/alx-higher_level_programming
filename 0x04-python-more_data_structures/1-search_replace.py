#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    if len(my_list) == 0:
        return my_list
    newlist = [i if i != search else replace for i in my_list]
    return newlist

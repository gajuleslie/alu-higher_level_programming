#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    return [replace if item == search else item for item in my_list]

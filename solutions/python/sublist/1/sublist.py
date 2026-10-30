"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    l1 = len(list_one)
    l2 = len(list_two)

    if l1==l2==0:
        return 3
    if l1==0:
        return 1
    if l2==0:
        return 2
        
    str_list_one = [str(item) for item in list_one]
    str_list_two = [str(item) for item in list_two]
    
    if l1>l2:
        if '.'.join(str_list_one).find('.'.join(str_list_two))!=-1:
            return 2
        else:
            return 4
    elif l1<l2:
        if '.'.join(str_list_two).find('.'.join(str_list_one))!=-1:
            return 1
        else:
            return 4
    else:
        if list_one==list_two:
            return 3
        else:
            return 4

        
        
        
    

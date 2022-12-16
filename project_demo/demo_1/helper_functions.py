
# functions that will be used in this project will be defined here

# to use variable import variables.py file
from demo_1 import variables as v1


def function(start, end):
    list_ = []
    for i in range(start, end):
        if i not in v1.SKIP:
            list_.append(i)
    return list_

def prettify(l):
    s = ""
    for i in l:
        s += "{} ".format(i)
    return s

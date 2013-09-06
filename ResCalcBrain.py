#! /usr/bin/python

"""
This Program is meant to aid in the choice of resistors,
showing only resistors that are available in certain
resistor series or user defined groups
"""

# ----- Imported Modules
import math
import string
import operator


# ----- Classes

class ResCombo(self):
    resCount = 0
    def __init__(self, R1, R2, Crnt, RtSd, diff):
        self.R1 = R1
        self.R2 = R2
        self.Crnt = Crnt
        self.RtSd = RtSd
        self.diff = diff
        ResCls.resCount+=1

# ----- User Defined Variables
perc = 0.01
# perc defines how close the reported value has to be to
# the calculated value

# ----- Functions
def convert(Value):
    # Converts User input string to floating point
    # number so calculations can be done on the inputs
    Value = Value.upper()
    if 'K' in Value:
        Value = string.strip(Value,'K')
        Value = float(Value)*math.pow(10,3)
    elif 'M' in Value:
        Value = string.strip(Value,'M')
        Value = float(Value)*math.pow(10,6)
    else:
        Value = float(Value)
    return Value

def removeDuplicates(l):
    # Removes Duplicate elements in the list that is passed
    # in by making it a set and then putting it back in a
    # list, sets can not have duplicates
    return(list(set(l)))

# ----- Main Loop
if __name__ == '__main__':


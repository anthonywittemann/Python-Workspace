#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(42)
    passFunc()
    manyArgsFunc(23, 24)

# optional arguments have default values
def testfunc(number, another = None, yetAnother = 5): 
    print('This is a test function', number, another, yetAnother)
    # testing for default value and can then after assign a value
    if another == None:
        another = 112
    print('This is a test function', number, another, yetAnother)
    
# this function serves as a stub to be filled in later
def passFunc():
    pass

def manyArgsFunc(*args):
    for index, arg in enumerate(args):
        print('Arg {}:'.format(index), arg)

if __name__ == "__main__": main()

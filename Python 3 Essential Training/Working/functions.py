#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
#     testfunc(42)
#     passFunc()
#     manyArgsFunc(23, 24)
#     namedArgsFunc(one = 1, two = 2)
    allTogether(1,2,23,24,one=1,two=2)

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
        
# kwargs = keyword arguements
def namedArgsFunc(**kwargs):
    print('kwargs: ', kwargs['one'], kwargs['two'])

# needs to be in the order regular params, *args and finally **kwargs
def allTogether(num1, num2, *args, **kwargs):
    print('Num1: ', num1, 'Num2: ', num2)
    for index, arg in enumerate(args):
        print('Arg {}:'.format(index), arg)
    print('kwargs: ', kwargs['one'], kwargs['two'])
    

if __name__ == "__main__": main()

#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# allows you to define functions after they are used
def main():
    #everything in python is an object an 
    a, b = 1, 0
    a, b = b, a # can swap variables without creating a temp!!
    print("This is the syntax.py file.", a, b)
    a = "one"
    print(type(a), a)
    a = (1, 2, 3, 4, 5) # tuple
    print(a)
    a = [1, 2, 3, 4, 5] # list
    print(a)
    
    # conditionals
    a, b = 0, 1
    if a < b:
        print("a < b")
    elif a > b:
        print("a > b") 
    else:
        print("a == b")
    
    # defining and using functions
    egg() # would not work if there were no main function
    func(3)
    func(12) # doesn't work
    func()

def egg():
    print("egg")
    
def func(a = 0): # default value to be assigned to a
    for i in range(a, 10):
        print(i, end=' ')


x, y = 0, 1
s = "<" if x < y else ">=" # conditional expression
print(s)

if __name__ == "__main__": main()

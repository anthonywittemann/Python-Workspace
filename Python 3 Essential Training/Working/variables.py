#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # integers and floating point #s
    print("This is the variables.py file.")
    num = 42
    print("Type: ", type(num))
    print("ID: ", id(num), num)
    num = 43
    print("ID: ", id(num), num) # id has changed b/c primitive data types are immutable
    num = 42
    print("ID: ", id(num), num)  # id has changed back to previous address b/c the 
                            # variable referenced the same object in both cases
    num = 42 / 9            # num is typecast as a FLOAT when dividing
    print("Division Type: ", type(num), num) 
    num = round(num)        # can round down
    print("Rounded Type: ", type(num), num) 
    num = 42 // 9            # integer division to typecast num as an int
    print("Integer Division Type: ", type(num), num) 
    num = float(num)        # typecasting is easy
    
    

if __name__ == "__main__": main()

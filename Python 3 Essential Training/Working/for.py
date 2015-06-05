#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line, end='') # instead of a /n after each print, we have nothing
    
    print('\n')
    
    for num in [1,2,3,4,5]: # in python any container object can function as an iterator
        print(num, end=' ') 
        
    print('\n')
    
    for index, letter in enumerate("word"): # iterator also now returns the index
        print(index, letter)
        if(letter == 'o'): print('Index {} is an o'.format(index))

if __name__ == "__main__": main()

#!/usr/bin/python3
# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    for c in s:
        if c=='i': continue # skip if an i
        if c=='g': break # stop looping if a g
        print(c, end='')
    else: # execute when for/while statement is false
        print('else')

if __name__ == "__main__": main()

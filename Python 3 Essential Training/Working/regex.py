#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open('raven.txt')
    
    # searching with regular expressions
    for line in fh:
        #find all the lines that have Lenore or Nevermore and print them
        if re.search('(Len|Neverm)ore', line):
            print(line, end='')
        
        #finding specific patterns in a set
        #prints out just the words
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())

    
if __name__ == "__main__": main()

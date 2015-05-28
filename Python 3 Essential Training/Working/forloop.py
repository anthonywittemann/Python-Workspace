#!/usr/bin/python3

# read the lines from the file
fh = open('lines.txt')
for line in fh.readlines(): # use of an iterator object
    print(line, end='') # new new line after print statement

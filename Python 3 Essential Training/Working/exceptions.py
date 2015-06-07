#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        # strips any trailing /n from the end of the string
        # and prints out each line - same as end=''
        for line in readfile('lines.txt'): print(line.strip())
    except IOError as e:
        print("something bad happened: ({})".format(e))
    except ValueError as ve:
        print('bad filename: ({})'.format(ve))
    else:
        print("after badness")
        # could also put everything from the else into the try

def readfile(filename):
    if filename.endswith('.txt'):
        fh = filename.open()
        return fh.readlines()
    else: raise ValueError('filename must end with .txt')

if __name__ == '__main__': main()

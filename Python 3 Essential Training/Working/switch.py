#!/usr/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth'
    )
    choice = 'one'
    print(choices[choice]) # this doesn't work when 
                        # the value supplied isn't in the dict
                        
    print(choices.get(choice, 'other')) # this fixes that problem
if __name__ == "__main__": main()

#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    # using a dictionary for multiple constructor parameters
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', 'white')
        self._v = kwargs.get('value', 42)
        self.variables = kwargs
    
    # what the above constructor is really doing
#     def __init__(self, value = None, color = 'white'):
#         self._color = color
#         self._v = value
#         print('constructor', self._v)
    
    def quack(self):
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)
    
    def getColor(self):
        return self._color
    
    def setColor(self, newColor):
        self._color = newColor
        
    def getVariable(self, k):
        return self.variables.get(k, None)
    
    def setVariable(self, k, v):
        self.variables[k] = v

def main():
    donald = Duck(value = 47, color = 'blue')
    print(donald) # donald is an object of class Duck
    donald.quack()
    donald.walk()
    frank = Duck(value = 151, feet = 2)
    frank.quack()
    frank.walk()
    print('feet:', frank.getVariable('feet'))

if __name__ == "__main__": main()

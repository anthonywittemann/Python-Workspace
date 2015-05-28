#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
class Fibonacci():
    # constructor optional - default constructor created if none defined
    def __init__(self, a, b): # __init__ constructor
        self.a = a
        self.b = b

    def series(self):   # self is a reference to the instantiated object
        while(True):
            yield(self.b)   # returns iterator for b
            self.a, self.b = self.b, self.a + self.b # multiple assignments on one line

# no main method needed, just starts execution
f = Fibonacci(0, 1)
for r in f.series(): # calls generator function series
    if r > 100: break    
    print(r, end=' ')


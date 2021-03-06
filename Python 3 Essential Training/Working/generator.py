#!/usr/bin/python3

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

# generator function - returns an iterator object which is used in function below
def primes(n = 1):
    while(True):
        if isprime(n): yield n  # yields returns a value like return, 
                                # but the next time the fn is called 
                                # the execution continues after the yield
        n += 1 

for n in primes():
    if n > 100: break
    print(n)


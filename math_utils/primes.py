from math import sqrt

def isprime(n):
    if n <= 1:
        return False

    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True
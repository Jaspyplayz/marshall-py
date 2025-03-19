# Lesson 36

def primeFactors(num):
    res = []
    for i in range(1, num):
        if isPrime(i):
            res.append(i)

    return res

import math

def isPrime(num):
    if num <=1:
        return False
    if num ==2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
        

    

    





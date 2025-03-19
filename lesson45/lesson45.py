# Lesson 45

def lenDict(arr):

    lenDict = {}

    for i in arr:
        
        lenDict[i] = len(i)

    return lenDict

words = ["apple", "banana", "cherry", "date", "elderberry"]

print(lenDict(words))

"""
def fib(n, memo= {0:0, 1:1}):
    
    if n not in memo:

        fib(n-1, memo)
        fib(n-2, memo)
        memo[n] = memo[n-1] + memo[n-2]

    return memo

print(fib(10))
"""

def fib(n):

    memo = {0:0, 1:1}

    for i in range(2, n+1):
        memo[i] = memo[i-2] + memo[i-1]

    return memo

    
            

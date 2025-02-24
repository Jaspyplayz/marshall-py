# Lesson 22

upper_limit = int(input("Enter N to find the Nth Fibonnaci Number: "))

fib_0 = 0
fib_1 = 1
fib_n = 0

for n in range(2, upper_limit+1):
    fib_n = fib_1 + fib_0

    fib_0 = fib_1
    fib_1 = fib_n

print(f"Fibonacci {upper_limit} is {fib_n}.")
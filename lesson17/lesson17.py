# Lesson 17

num = int(input())

n = num - 1
while n > 0:
    num = num * n 
    n = n - 1

print(f"{num}")
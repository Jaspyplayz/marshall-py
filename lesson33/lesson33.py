# Lesson 33

def median(a_list):
    a_list = sorted(a_list)

    sum = 0
    for num in a_list:
        sum += num
    
    mean = sum / len(a_list)

    median = 0

    if len(a_list) % 2 == 0:
        median = (a_list[len(a_list) // 2] + a_list[len(a_list) // 2 - 1]) / 2
    else:
        median = a_list[len(a_list) // 2]

    print(mean)
    print(median)

from random import seed
from random import randrange

seed(2)
data = [randrange(1, 100) for _ in range(randrange(10,30))]
print(data)
median(data)

    

   
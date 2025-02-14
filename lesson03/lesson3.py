#import statements
from math import sqrt, floor

# Lesson 3
tiles = int(input()) #int() is a type of casting Function that converts its argument to integer

#processing 

# answer = tiles ** 0.5
# answer = floor(sqrt(tiles))
answer = sqrt(tiles)
answer = floor(answer)

#output

print(f"The largest square had a side length of {answer}.")


from math import ceil
# Lesson 4

#Input
section1 = input("Enter section 1: ")
section2 = input("Enter section 2: ")
section3 = input("Enter section 3: ")

#Processing 

cans = len(section1) + len(section2) + len(section3)

cansReq = ceil(cans / 12)

leftOver = cansReq*12-cans

price = cansReq * 14.95

#Output

print(cansReq)
print(leftOver)
print(price)


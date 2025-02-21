# Lesson 11

point = input()

point = point.split(' ')

point = list(map(int, point))
print(point)

x, y = point
print(f'x is {x}')
print(f'y is {y}')

if x > 0:
    if y > 0:
        print("Quadrant 1")
    else:
        print("Quadrant 4")
else:
    if y > 0:
        print("Quadrant 2")
    else: 
        print("Quadrant 3")
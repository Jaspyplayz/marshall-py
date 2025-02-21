# Lesson 12


angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

angle_sum = angle1 + angle2 + angle3

if angle_sum != 180:
    print("Error")
else:
    if angle1 == angle2 == angle3:
        print("The triangle is equilateral")
    elif angle1 != angle2 and angle1 != angle3 and angle2 != angle3:
        print("The triangle is scalene")
    else:
        print("The triangle is Iscosceles")

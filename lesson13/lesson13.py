# Lesson 13

month = int(input())
day = int(input())

if month == 2 and day == 18:
    print("Special Day")
elif month == 1 or (month == 2 and day < 18):
    print("Before")
else:
    print("After")

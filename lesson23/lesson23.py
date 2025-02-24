# Lesson 23

loop = True

total_sum = 0
counter = 0

while loop:

    user_input = input()

    if user_input.lower().capitalize() == "Exit":
        loop = False
        break
    else:
        mark = int(user_input)
        if 0 <= mark <= 100:
            total_sum = total_sum + mark
            counter += 1
        else: 
            print("Invalid input")

average = total_sum/counter

print(f"Your average is: {average}")
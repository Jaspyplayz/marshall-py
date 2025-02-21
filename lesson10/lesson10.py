# Lesson 10

teleNum = ''

for i in range(4):
    teleNum = teleNum + input()

print(f"{teleNum}")

if phone[0] in {'8', '9'}:

    if phone[-1] in {'8', '9'}:
        if phone[1] == phone[2]:
            print(f"The phone number with {phone} as its last four digits is a telemarketer")
        else:
            print(f"The phone number with {phone} as its last four digits is not a telemarketer")

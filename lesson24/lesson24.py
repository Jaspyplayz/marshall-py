# Lesson 24



loop = True
longestName = ""
longestNum = 0

while loop:
    str = input()

    if(str.lower().upper() == "X"):
        loop = False
        break
    else:
        if len(str) > len(longestName):
            longestName = str
            longestNum = len(str)
        
print(f"The longest name is {longestName} with {longestNum} letters")
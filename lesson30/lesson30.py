# Lesson 30

def pattern(n):

    for i in range(1, n+1):
        for j in range(1, i+1):
            if j % 2 != 0:
                print("1", end = "")
            else:
                print("0", end = "")

        print ("")

pattern(int(input()))
        


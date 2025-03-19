dict = {}

while True:
    
    score = 0
    n = input().lower()
    
    if(n == "x"):
        break
    elif(n not in dict):
       
        for i in range(len(n)):
            if n[i].isalpha():
                if n[i] in "aeiou":
                    score += 1
                else:
                    score += 5
    
        score = score * len(n)
        dict[n] = score
        highest = max(dict.values())
        lowest = min(dict.values())

print(f"Your highest value is: {highest}")
print(f"Your loweset value is: {lowest}")
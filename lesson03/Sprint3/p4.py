bronze_counter = 0
num = int(input())
gold = silver = gold = -1
scores = []

for i in range(num):
    score = int(input())
    scores.append(score)

    if score > gold:
        bronze = silver
        silver = gold
        gold = score
        
    elif score > silver and score != gold:
        bronze = silver
        silver = score
        
    elif score > bronze and score != silver and score != gold:
        bronze = score
       
bronze_counter = scores.count(bronze)
       

print(f"{bronze} {bronze_counter}")


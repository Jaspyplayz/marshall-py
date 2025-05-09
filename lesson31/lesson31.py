# Lesson 31

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(t[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

print(isAnagram(input(), input()))
# Lesson 38
def largestPalindrome():

    maxPalindrome= 0
    for i in range(999):
        for j in range(i, 999):
            if isPalindrome(str(i*j)):
                maxPalindrome = max(maxPalindrome, i*j)

    print(maxPalindrome)
def isPalindrome(text) -> bool:

    if len(text) == 1:
        return True
    else:
        
        mid = len(text) // 2

        for i in range(mid):
            if text[i] != text[-1*i-1]:
                return False

        return True
    
largestPalindrome()
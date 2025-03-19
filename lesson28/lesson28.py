# Lesson 28

def palindrome_checker(text) -> bool:

    if len(text) == 1:
        return True
    else:
        
        mid = len(text) // 2

        for i in range(mid):
            if text[i] != text[-1*i-1]:
                return False

        return True

print(palindrome_checker(input()))
# Lesson 27

def string_cleaner(s):
    
    str = ""
    
    if len(s) == 0:
        return -1
    else:
        for i in s:
            if i.isalpha():
                str += i.lower()
        return str

    
value = string_cleaner(input())
print(value)

        
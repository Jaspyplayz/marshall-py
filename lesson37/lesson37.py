# Lesson 37

def stringCompress(text):
    if not text:
        return ""

    compressedString = ""

    count = 1
    for i in range(1,len(text)):
        if text[i] == text[i-1] and text[i]:
            count += 1
        else:
            compressedString += f"{text[i-1]}{count}"
            count = 1
    
    compressedString += f"{text[-1]}{count}"
    print(compressedString)




stringCompress("aabcccccaaa")
    


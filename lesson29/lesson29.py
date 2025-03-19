# Lesson 29

def consonant_counter(text):

    counter = 0

    text = text.lower()

    for i in text:
        if i.isalpha():
            if i not in "aeiou":
                counter += 1
    
    return counter

print(consonant_counter(input()))

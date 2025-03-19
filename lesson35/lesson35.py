# Lesson 35

def removeDuplicates(text):

    list = []

    for i in text:
        if i not in list:
            list.append(i)

    return list
            
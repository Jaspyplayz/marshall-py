# Lesson 34

def csv_to_list(text):

    csv = text.split()
    a_list = []

    for item in csv:
        a_list.append(int(item))

    return a_list

    

from random import randrange

def rand_list(start, end, frequency):
    if start < end and frequency > 0:
        a_list = []
        for _ in range(frequency):
            new_value = randrange(start, end+1)
            a_list.append(new_value)
        return a_list
    else:
        return []
    

    


 
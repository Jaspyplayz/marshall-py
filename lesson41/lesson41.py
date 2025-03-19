# Lesson 41

scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
    'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
    'Z': 10}


def scrabble_score(text):

    score = 0
    if not text:
        return 0
    elif len(text) == 7:
        return 50
    else:
        for char in text.upper():
            if char.isalpha():
                score += scores[char]

    return score

def best_score(arr):
    res_list = ["", 0]

    for word in arr:
        
        curr_score = scrabble_score(char)

        if curr_score > res_list[1]:
            res_list[0] = word
            res_list[1] = curr_score

print(scrabble_score(input()))



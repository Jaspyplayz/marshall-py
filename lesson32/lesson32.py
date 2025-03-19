# Lesson 32

def duplicates(word1, word2):

    if not word1 or not word2:
        return []
    
    set_word1 = set(word1)
    set_word2 = set(word2)

    result = []
    for n in set_word1:
        if n in set_word2:
            result.append(n)

    return sorted(result)

print(duplicates(input(), input()))
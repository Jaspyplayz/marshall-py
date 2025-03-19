# Lesson 44

def freq(text):

    freq = {}

    for char in text:

        if char in freq:
            freq[char] = freq.get(char, 0) + 1
        else:
            freq[char] = 1

    freq = {key: freq[key] for key in sorted(freq)}
    return freq

print(freq("fortniteballs"))


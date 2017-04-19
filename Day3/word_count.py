from collections import Counter
"""
A function that counts the occurrences or characters in a word
"""


def words(phrase):
    if isinstance(phrase, str):
        words_list = phrase.split()
        word_occurrences = dict(Counter(words_list))
        for key in word_occurrences.keys():
            try:
                int(key)
                word_occurrences[int(key)] = word_occurrences.pop(key)
            except ValueError:
                continue
        return word_occurrences
    else:
        raise TypeError('Argument should be string')

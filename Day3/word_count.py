from collections import Counter
"""
A function that counts the occurrences or characters in a word
"""


def words(phrase):
    # Check that the argument passed into function is a string
    if isinstance(phrase, str):
        # Split the phrase into individual words and add them to a list
        words_list = phrase.split()
        # Use Counter from the collections module to count occurrences of words in list
        # Convert counter object into a dictionary
        word_occurrences = dict(Counter(words_list))
        return word_occurrences
    else:
        raise TypeError('Argument should be string')

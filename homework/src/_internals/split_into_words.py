import re


def split_into_words(lines):
    words = []
    for line in lines:
        words.extend(word.strip(",.!?") for word in line.split())
    return words  # Return an iterator over the list of words

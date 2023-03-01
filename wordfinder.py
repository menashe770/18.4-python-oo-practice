"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Find random words from a dictionary

    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, path):
        # Open the dictionary file and store the file object
        dict_file = open(path)
        # Parse the file and store the list of words
        self.words = self.parse(dict_file)
        # Print the number of words read from the file
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        # Strip whitespace from each line in the file and return as a list
        return [word.strip() for word in dict_file]

    def random(self):
        # Return a random word from the list of words
        return random.choice(self.words)

"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Find random words from a dictionary.

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
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


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments."""

    def parse(self, dict_file):

        words = []

        # Iterate through each line in the file
        for line in dict_file:
            # Strip any whitespace from the line to get the word
            word = line.strip()

            # Check if the word is not empty and does not start with a hash character
            if word and not word.startswith("#"):
                # If the word is valid, add it to the list of words
                words.append(word)

        # Return the list of valid words
        return words

        # return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]

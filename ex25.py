# defining a function which will take one string argument
def break_words(stuff):
    """This function will break a sentence into words"""
    # using .split() method of string, we are going to break the input sentences into separate words
    # .split() and .strip() are two different methods of string class
    words = stuff.split()
    # returning all seperated words as output of function
    return words

# defining a function which will take input of seperated words and will sort them alphabetically
def sorted_words(words):
    """This function will sort the words"""
    # sorted() function directly sort the strings
    return sorted(words)

# defining a function to take out one word out of a list of words by specifying its position in list using .pop() method of string
def print_first_word(words):
    """Print the first word after popping it off"""
    # Here, using pop() method, we are choosing word at position 0, which is first position in any object.
    word = words.pop(0)
    print(word)

# defining a function to take out one word out of a list of words by specifying its position in list using .pop() method of string
def print_last_word(words):
    """Print the last word after popping it off"""
    # Here, using .pop() method, we are choosing word at last position, although u may or may not sure of string length, so -1 is a position which starts reading string backward
    # -1 is last from left to right, while first from backward
    # -2 is second last, while interpreting from right to left
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in full sentence and returns the sorted words"""
    # calling a function inside a function
    words = break_words(sentence)
    return sorted_words(words)


def print_first_and_last_word(sentence):
    """Print the first and last word of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted_word(sentence):
    """Print the first and last sorted words"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

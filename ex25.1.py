#import ex25
from ex25 import *
sentence = "All good things come to those who wait."
#words = ex25.break_words(sentence)
words = break_words(sentence)
print(words)
#sorted_words = ex25.sorted_words(words)
sorted_words = sorted_words(words)
print(sorted_words)
#ex25.print_first_word(words)
#ex25.print_last_word(words)
print_first_word(words)
print_last_word(words)
print(words)
#ex25.print_first_word(sorted_words)
#ex25.print_last_word(sorted_words)
#ex25.print_first_and_last_word(sentence)
#ex25.print_first_and_last_sorted_word(sentence)
print_first_word(sorted_words)
print_last_word(sorted_words)
print_first_and_last_word(sentence)
print_first_and_last_sorted_word(sentence)

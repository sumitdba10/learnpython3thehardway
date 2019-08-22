print("How old are you?", end=' ')
age = input()
print("How tall are you in inches?",end=' ')
height = input()
print("How much do you weigh in lbs?",end=' ')
weight = input()

# end=' ' at the end of each print line. This tells print to not end the line with a newline character and go to the next line.
print(f"So, you're {age} old, {height} inches tall, and {weight} pounds heavy.")
print("#"*50)

################################################################################

#ex12.py
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much you weigh? ")

print(f"So, you're {age} old, {height} inches tall, and {weight} pounds heavy.")
print("#"*50)

###############################################################################

#ex13.py

# importing a feature from Python feature statement
#argv is argument variable, it holds arguments as value
from sys import argv

script, first, second, third = argv

print("The script is called:",script)
print("The first variable is:",first)
print("The second variable is:",third)
print("The third variable is:",third)

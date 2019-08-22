
#ex13.py
# another way to take user input


# importing a feature (modules) from Python feature statement
#argv is argument variable, it holds arguments as value
from sys import argv

script, first, second, third = argv

print("The script is called:",script)
print("The first variable is:",first)
print("The second variable is:",second)
print("The third variable is:",third)
print("So, Please provide below mentioned personal details:")
print("\t*",first)
print("\t*",second)
print("\t*",third)

first = input("How old are you? ")
second = input("How tall are you? ")
third = int(input("How much you weigh? "))


print(f"So, you're {first} old, {second} tall, and {third} lbs heavy.")

# to run this program, we need to provide four arguments to python3.7 calling
# e.g. python3.7 ex13.py 1st 2nd 3rd

#Mistake #3

# we have to pass exact number of argument to unpack the argv (argument variable), less or more will throw error.

"""Sumits-MacBook-Pro:learnpython3thehardway sumitkannu$ python3.7 ex13.py name height weight age
Traceback (most recent call last):
  File "ex13.py", line 10, in <module>
    script, first, second, third = argv
ValueError: too many values to unpack (expected 4)
Sumits-MacBook-Pro:learnpython3thehardway sumitkannu$ python3.7 ex13.py name height
Traceback (most recent call last):
  File "ex13.py", line 10, in <module>
    script, first, second, third = argv
ValueError: not enough values to unpack (expected 4, got 3)"""


"""
What’s the difference between argv and input()? The difference has to do with where the user is required to give input.
If they give your script inputs on the command line, then you use argv.
If you want them to input using the keyboard while the script is running, then use input()."""

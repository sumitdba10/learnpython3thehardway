# This program is to exercise all previous learnings of print, string, escape sequences, multiple line string, f-string, format string, function, return, mathematical operations etcself.
# Printing string using "" and ' together
print("Let's print everything.")
# Printing string using escape sequences
print('you\' d need to know \'bout escapes with \\ that do: ')
# Printing new line escaping sequence to print string in a new line. Also, \t is tab escape sequence to put a tab space bar in front of a line of string
print('\n newlines and \t tabs.')

# using """ triplet of double quotes allow multiple lines in paragraph of string
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------------------------")
print(poem)
print("--------------------------------")

# performing mathematical operation using operators and converting result into integer using int method and finally saving result in 'five' variable
five = int(((((10 - 2) + 12) * 2) / 8))
# using f-string formatting, we can add variables within string
print(f"This should be five: {five}")

# defining function with one argument i.e. started
def secret_formula(started):
    # performing mathematical operation on argument and assigning result to a variable
    jelly_beans = started*500
    # using above variable, performing another mathematical operation and saving result to another variable
    jars = jelly_beans /1000
    # same as above step
    crates = jars/100
    # now function is returning values of three variables assigned above as output of function
    return jelly_beans, jars, crates

# assigning a variable with value
start_point = 10000
# This tricky, we are assigning output of our function to three variables in a consequitive fashion. 1st value will be assigned to first variable, and second will be assigned to second variables
# and so on.
beans, jars, crates = secret_formula(start_point)

# Now we are ingesting a variable into an string using another method ".format()" instead of f-string
print("With a starting point of: {}".format(start_point))
# using, f-string method to ingest into string
print(f"We'd have {beans} jelly_beans, {jars} jars, and {crates} crates")

# we can reasign variable after performing any operation to same variable name
start_point = start_point/10

print("We can also do this way:")
# saving output of function into a variable
formula = secret_formula(start_point)
# Now, if we have multiple comma seperated output of a function, we can ingest output into string while passing (*variable) 
print("We 'd have {} beans, {} jars, and {} crates.".format(*formula))

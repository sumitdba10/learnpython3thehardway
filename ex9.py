# more exercise to learn to print string

days = "Mon Tue Wed Thu Fri Sat Sun"
# assigning variable "Months" values, "\n" stands for new line, so each value will be printed in new line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

# mistake 2:
# I assigned variable Months but were calling variable months in print statement, variable should be matched


# printing a string and concatenating variable afterwards
print("Here are the days: ",days)
print("Here are the months",months)

# We can write numerous line as is using triple double quotes (""")
print(""" We can write numerous lines using triple double quotes
e.g. line 1
line 2
line 3
line 4
and so on ....""")

#vs
# we can't print multiple lines using single "" or '' within print statement
print("We can write numerous lines using triple double quotes
e.g. line 1
line 2
line 3
line 4
and so on ....")

# error:
"""
Sumits-MacBook-Pro:learnpython3thehardway sumitkannu$ python3.7 ex9.py
  File "ex9.py", line 25
    print("We can't write numerous lines using triple double quotes
                                                                  ^
SyntaxError: EOL while scanning string literal"""

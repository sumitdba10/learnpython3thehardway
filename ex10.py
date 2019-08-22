
# backslash t "\t" is to escape character using tab (space)
tabby_cat = "\tI'm tabbed in."

# \n new line escape character, any string after \n will print in new line
persian_cat = "I'm split \non a line."

# \ escape for '\' which is part of string we are printing. '\' used for escape a character but in below line we want to print \ as character, so we have used
# \ before \
backslash_cat = "I'm \\ a \\ cat."

# multiple line statement, creating a list, using tab for making bullet points
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

# \t* Catnip\n\t* Grass = first tab, "Catnip" string, then \n new line, then \t tab, then "* Grass" string

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

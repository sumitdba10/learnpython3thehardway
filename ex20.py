# from sys package, we are importing argument variables module
from sys import argv
import os

# asigning two variables to argv module
script,input_file = argv

# defining a function to read all content of a file
def print_all(f):
    print(f.read())

# defining a function to reset pointer to 0 position
def rewind(f):
    f.seek(0)

# defining a function to read one line from file
def print_a_line(line_count, f):
    print(line_count,f.readline())

# defining a function to append the existing file with new entries, and save it using close() method of file class
def write_to_file(f):
    f.write(input())
    f.write("\n")
    f.close()


# opening file and saving contents to variable
current_file = open(input_file)

print(f"First let's print the content of whole file {input_file}: ")
print("\n")
# while using f formatting method, how can we use \n formatter in string
# calling print_all function to print all the content of file
print_all(current_file)


print("Now, Let's rewind, kind of like a tape \n")
rewind(current_file)


print("Let's print three lines.\n")
current_line =1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)

# opening file in append mode
current_file = open(input_file,"a")
print(f"Add a new line to {input_file} file.")
# now as file is append mode, we can write new contents to it
write_to_file(current_file)
print("\n")

# As file was in write mode, we would not be able to read it directly, So opening same file in read mode
current_file = open(input_file,"r")
# printing all contents
print_all(current_file)

#######################################################################
# Questions for future:
# How can I delete specific line from a input_fileself.
# How can I edit the content of exisiting file.

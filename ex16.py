# Learn all functions of file in python - file.open(), file.read(), file.truncate, file.close(), file.write(value)

# from sys package importing argv (argument variable) module
from sys import argv
# assigning two variables to argv module
script, filename = argv

# using 'filename' variable in print string
print(f"We are going to erase the {filename}")
# if user will CTRL+C, python CLI will exit
print("If you don't want this, please hit CTRL+C (^C)")
# if user will hit enter/return, program will continue
print("If you do want that, hit RETURN/ENTER")
# taking user input
input("?")

print("Opening the file.......")
#opening the file in write mode
fileltchw = open(filename,'w+')


print("Truncating the file. Goodbye!")
# truncating the content of file
fileltchw.truncate()

print("Now, I am going to ask you to provide three lines about your career interest.")
# asking for user input
line1 = input('Interest 1: ')
line2 = input('Interest 2: ')
line3 = input('Interest 3: ')


print("Let's note down, your three interests to the file.")

# writing all user inputs into file

fileltchw.write(line1)
# introducing an empty line
fileltchw.write("\n")
fileltchw.write(line2)
fileltchw.write("\n")
fileltchw.write(line3)

print("\n")
print("Please validate your input in the file.")
# opening again file in read mode, we cannot read file variable directly, because file was opened in write mode only before.
fileltchw = open(filename,'r')
print(fileltchw.read())

print("\n")
print("Is everything good?")
confirm = input("Yes or No ")

# using if else condition to perform conditional tasks
# if elif else
if confirm == 'yes' or confirm == 'Yes' or confirm == 'YES':
    print("Yay!")
    print("Finally, saving and closing the file.")
    # finally, close method will save the content and close the file
    fileltchw.close()
else:
    fileltchw = open(filename,'w')
    fileltchw.truncate()
    print("file erased. Please re-run the program. Thanks.")

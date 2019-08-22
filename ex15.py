# So, In this program, we will be learning different ways to accept user inputs

#1. argv = argument variable: while executing script in shell or CLI, user have to pass value to arguments assigned to argvself.
#2. input = using input function, we can ask user to prompt their input value and can be stored in a variable for later useself.
#3. open =  user can store their input in a file, open in program using open() function and can read the file texts by using .read() method of file


#importing module argv which is part sys module package
from sys import argv
# assigning two variables for input of user to argv modules
script,filename,filename2 = argv

# from above line, we are using filename argument to recieve filename during script execution
# So we have two argument, script (current .py in which we are wroking), and filename (user will provide)

# now using open method, open the files and save in variable txt
txt = open(filename)

print(f"Here is your file {filename}")
# Now using read method of file, read and display the contents of file from txt variable
print(txt.read())

#print("Enter a file name:")
#file_new = input("> ")

#text_new = open(file_new)
#print("Days in a week:")
#print('-'*60)
#print(text_new.read())

# asking for user input using input fuction and storing in variable
user_name = input("Please print your name:")
#dream_company = input("What's your dream company to work for?")
print(f"Thanks {user_name}, Listen carefully.")

# opening file and storing in variable for later use
txt2 = open(filename2)
#print(f"Listen {user_name}"")
print(txt2.read())

# importing module argv (argument variable)
from sys import argv

#
script,user_name = argv
prompt = '> '

#printing string, while using f formatting to put  variables user_name, and script inside the string
print(f"Hi {user_name}, I m 'm the {script} script.")
print("I'd like to ask you few questions.")
print(f"Do you like me {user_name}?")
# asking for user input from keyboard while prompting prompt variable on user screen and storing input in likes variable
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")



print(f"Hey,{user_name} would you like to become an employee at Google?")
employee = input(prompt)

print("So, Are you preparing Algorithms, Programming, and Data Structure?")
learning = input(prompt)

if employee == 'no':
    print("So, as answer is no for employment, No worries")
elif employee == 'yes':
    print(f"{user_name}, you're on right track. Good Luck")
else:
    print("Input is invalid, please enter yes or no")

if employee == 'yes' and learning == 'no':
    print("So, As your answer is no for preparation, please start it rightaway")
elif employee == 'yes' and learning == 'yes':
    print(f"{user_name}, you're on right track. Good Luck")
elif employee =='no' and learning == 'no':
    print(f"Bye, {user_name}")
else:
    print("Input is invalid, please enter yes or no")


""" So, If answer is No for employment, No worries.
If your answer is No for preparation, please start it rightaway.
if your answer is yes for preparation, then you are on right track. Good Luck.
As your answer is {learning}, you know where you stand. Thanks."""

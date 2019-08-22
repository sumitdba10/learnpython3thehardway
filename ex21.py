# Functions may return something

# defining a function for addding two variables
def add(a,b):
    #a = int(input())
    #b = int(input())
    print(f"ADDING {a} + {b}: ")
    return a+b

# defining a function for subtracting two variables
def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}: ")
    return a-b

# defining a function for multiplying two variables
def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}: ")
    return a*b

# defining a function for dividing two variables
def divide(a,b):
    print(f"DIVIDING {a} / {b}: ")
    return a/b

print("Let's do some math with functions")

# calling functions, and saving return result into variables
# Question: How can we ask for user input in function
#sol: using input() function for each argument of function, we can input from screen
print("Let's find out your age using add math function")
age = add(int(input("Enter first number: ")),int(input("enter Second number: ")))
print("Let's find out your height using subtract math function")
height = subtract(int(input("Enter first number: ")),int(input("enter Second number: ")))
print("Let's find out your weight using multiplication math function")
weight = multiply(int(input("Enter first number: ")),int(input("enter Second number: ")))
print("Let's find out your iq using divide math function")
iq = divide(int(input("Enter first number: ")),int(input("enter Second number: ")))

#f formatting


names = input(" What's your name? ")
print("\nyour stats:")
print(f"Hey Mas. {names} \t* Age: {age} years old, Height: {height} cms, Weight: {weight} lbs, and IQ: {iq}")


print("\nHere is a puzzle")

#PEMDAS rule for functions and storing in a variable
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# printing strings, and function
print("That become: ", what, "Can you do it by hand?")

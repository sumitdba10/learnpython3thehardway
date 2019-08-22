#This program is to understand assigning of variables, and format of string while using assigned variables

#assigning some variables

name = 'Sumit Dhama'
age = 32.5
height = 74
weight = 174
eyes = 'Brown'
teeth = 'White'
hair = 'Dark Brown'
# converting pounds to kilograms
# 1 pound =  0.45359237 kg
# 10 pound = 4.535 kg
# 1 kg = 2.20 pounds
# 10 kg = 22 pounds
weight_in_kg = round(weight*0.45359237)

# converting inches to centimeters
# 1 inch = 2.54 centimeters
# 74 inches = 187.96 centimeters
# 1 cm = 0.3937 inches
# 12 inches = 12*0.3937 cms =  30.48 cms
height_in_cms = round(height*0.3937)


print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print("or")
print(f"He's {height_in_cms} cms tall.")
print(f"He's {weight} pounds heavy.")
print("or")
print(f"He's {weight_in_kg} kg heavy.")
print("Actually that's right weight as per height")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"He's teeth are usually {teeth} depending upon on the coffee.")
print("\n")

#This time we are going to perform mathematical operations with assigned variables
total = age+height+weight
print(f"If we add his age, height, and weight we get {total}.")
print("\n")

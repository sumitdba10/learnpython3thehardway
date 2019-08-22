types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = 'binary'
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said:{x}")
print(f"I said:{y}")

hillarious = False
joke_evaluation = "Isn't the joke so funny! {}"

print(joke_evaluation.format(hillarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w+e)

first_name = "Sumit"
last_name = "Dhama"
spouse_first_name = "Deepika"
spouse_last_name = "Choudhary"

couples = "{} {} has got married to {} {} in 2015."

print(couples.format(first_name,last_name,spouse_first_name,spouse_last_name))
print(couples.format(spouse_first_name,spouse_last_name,first_name,last_name))

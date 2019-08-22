# Names,Variable,Code, Functions

# this program is to learn functions in Pythonself.

def print_two(*args):
    arg1, arg2 = args
    print(f"Husband:{arg1} & Wife:{arg2}")



def print_two_again(arg1, arg2):
    print(f"Husband:{arg1} & Wife:{arg2}")


def print_one(arg1):
    if arg1 == 'Deepika-Choudhary':
        print(f"Wife:{arg1}")
    else:
        print(f"Husband:{arg1}")


def print_none():
    print("I got nothing to print!")


def replace_battery(years):
    if years >= 3 and years <= 4 :
        print("You may wanna replace battery!")
    elif years > 4:
        print ("We highly recommend to replace battery as soon as possible!")
    else:
        print ("No need to worry about battery yet!")



print_two("Sumit-Dhama", "Deepika-Choudhary")
print_two_again("Sumit-Dhama", "Deepika-Choudhary")
print_one("Sumit-Dhama")
print_none()
replace_battery(int(input("How old is your battery? ")))

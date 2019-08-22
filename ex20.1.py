from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count,f):
    print(line_count,f.readline())


def write_to_file(f):
    user_input = input("Enter your line: ")
    #print(len(user_input))
    if len(user_input) > 0:
        f.write(user_input)
        f.write("\n")
        f.close()
    else:
        print("\nNothing will be adding!")



current_file = open(input_file,'r+')

print(f"Let's print the content of the {input_file} file")
print_all(current_file)

print("Let's rewind, Kind of like a tape \n")
rewind(current_file)


print("Now, Let's print some lines from file \n")

current_count =1
print_a_line(current_count,current_file)

current_count+=1
print_a_line(current_count,current_file)

current_count+=1
print_a_line(current_count,current_file)

print("\n")

current_file = open(input_file, 'a+')
print(f"Now let's add a line to {input_file} file: ")
write_to_file(current_file)
print("\n")

current_file = open(input_file,'r+')
print_all(current_file)

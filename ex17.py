#importing argv module from sys package to take user input from CLI
from sys import argv
# importing exists module from os.path package to check if a file exists in OS before writing or reading
from os.path import exists

# assigning two variables to argv argument, now we user have to provide three arguments while running script i.e. script, file from and to file.
script, from_file, to_file = argv

# printing string using f string function with above defined variables
print(f"Copying data from {from_file} to {to_file}.")

#in_file = open(from_file)
#indata = in_file.read()
# opening file, and reading the content
indata = (open(from_file)).read()

# using len method of string to get value in bytes
print(f"The input file is {len(indata)} bytes long.")
# using exists module to check if file exists in OS
print(f"Does the output file exist? {exists(to_file)}")
print("Ready? Hit enter/return to continue, CTRL-C to abort")
# asking for some user input
input()
# opening file in write mode, and storing in variable for later use
out_file = open(to_file,'w')
# writing the content of 'indata' variable to output file
out_file.write(indata)

print("Alright, all done")
# finally, closing the file or saving plus closing
out_file.close()
#in_file.close()

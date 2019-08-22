# printing a string
print("Marry had a little lamp.")
# printing a string using dot format function, embedding string inside a string
print("Its fleece was white as {}".format('snow'))
# printing a string
print("And everywhere that Mary went.")
# printing a string and multiplying times using * (multiplying operator), below line will print '.' 10 times
print("."*10)

#Bunch of variable assignments
end1='C'
end2='h'
end3='e'
end4='e'
end5='s'
end6='e'
end7='B'
end8='u'
end9='r'
end10='g'
end11='e'
end12='r'

# Printing concatenation of all variables assigned above, because we want to keep continous printing, we have used end = ' ' in single lines
# with end=' ' will result in Cheese Burger while without end=' ' the result would be
#Cheese
#Burger
print(end1+end2+end3+end4+end5+end6,end=' ')

# my mistake #1
# printing variables using ',' will create space betweeb each variables
# e.g. B u r g e r


#print(end7,end8,end9,end10,end11,end12)

# solution
# while printing variables with '+' will keep together all variables
print(end7+end8+end9+end10+end11+end12)

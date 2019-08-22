
# assiging a string variable four values but empty
formatter = "{}, {}, {}, {}"

# printing string assigned above, assigning values in a sequence using dot format function, arguments for format function of String are numbers
print(formatter.format(1,2,3,4))
# printing string assigned above, assigning values in a sequence using dot format function, arguments for format function of String are strings
print(formatter.format("one","two","three","four"))
# printing string assigned above, assigning values in a sequence using dot format function, arguments for format function of String are boolean values
print(formatter.format(True,False,False,True))
#printing string assigned above, assigning values in a sequence using dot format function, arguments for format function of String are variable itself
print(formatter.format(formatter,formatter,formatter,formatter))
#printing string assigned above, assigning values in a sequence using dot format function, arguments for format function of String are some text together makes a paragraph
print(formatter.format("You're dying", "You're dying a little more everyday", "because deep down you're giving up your dream","It's worth to know!"))

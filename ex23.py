# importing sys package
import sys

#assigning three variables to argv (argument variable) module
# script : this whole program as .py
# encoding : variable to define encoding e.g. unicode - utf8/utf16/utf32 or ASCII etcself.
#error : to store errors
script,encoding, errors = sys.argv

# defining a function with 3 arguments , the input file, encoding and errors
def main(language_file,encoding, errors):
    # reading lines from file and assigning to a Variable
    line = language_file.readline()

    # if condition, if we have a line in file then
    if line:
        #execute the print_line function which is defined below
        print_line(line,encoding,errors)
        # also, return main function again to continue with readline
        return main(language_file,encoding,errors)


def print_line(line,encoding,errors):
    # we are using line variable from main function above, using .strip() function of a string we strip both trailing and leading whiespaces are removed from string
    next_lang = line.strip()
    # raw bytes is a sequence of bytes that python uses to store utf-8 encoded string
    # next_lang is a variable which has stripped line from language input input_file
    # we are encoding each line in raw bytes using encode method
    raw_bytes = next_lang.encode(encoding,errors=errors)
    # we are decoding raw bytes to utf-8 string using decode method
    cooked_string = raw_bytes.decode(encoding,errors=errors)
    # Now printing bytes encoding and utf-8 character equivalent to each other
    print(raw_bytes, '<====>',cooked_string)

# opening input file in utf-8 unicode encoding
languages = open("languages.txt",encoding ="utf-8")
# Now finally calling main function
main(languages,encoding,errors)

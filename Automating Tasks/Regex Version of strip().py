#Regex Version of strip()

'''
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string.
'''

import re

stripChar = input('Enter character to strip: ')
context = input('Enter string to strip: ')

#function to strip the string of the character user provided
def strip(char, string):
    #when user input empty character to be stripped
    if char == "":
    	#we strip away space \s character from front and end of the string
        regsp = re.compile(r'^\s+|\s+$')
        stripContext = regsp.sub("", string)
        return stripContext
    else:
    	#but if user inputs actual character to be stripped then we strip that character
        stripContext = re.sub(r'^{}+|{}+$'.format(char,char), "", strip("",string))
        return stripContext

print(strip(stripChar, context))

input('Enter any key to continue:)')

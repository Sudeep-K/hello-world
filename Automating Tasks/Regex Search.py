#! python3
#Regex Search
'''
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.
'''

#import os for file handling, re for regex expression module
import os, re

#loop over each file to read it's content and save it to 'text' variable
for file in os.listdir('F:\\python'):
	fileObject = open('F:\\python\\{}'.format(file))
	text = fileObject.read()
	fileObject.close()

	#prompt user to enter the regular expression
	regularEx = input('Enter your regular expression.')

	#match the regular expression to the 'text' obtained from our.txt file
	regexObj = re.compile(r'{}'.format(regularEx))
	print(regexObj.findall(text))

#ignore
input('Enter \'ENTER\' key to quit (:')
#Strong Password Detection

'''Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple 
regex patterns to validate its strength.'''

#takes the password input by user as a string
stringUser = input('''Please, Enter a strong password consisting of atleast 8 characters,
 contains both upper and lower case and atleast a digit''')

#importing re module
import re

#user defined function to check if the password is strong or not
def strongPasswordDetector(text):

	#TODO: length validator that check the length of password supposed to be 8 characters or long
	lengthRegex = re.compile(r'.{8,}')
	if not (lengthRegex.findall(text)):
		return print('Not enough characters, your password must be atleast 8 characters long.')

	#TODO: uppercase and lowercase validator that validates if the password has both upper and lower case or not
	upperlowerRegex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])')
	if not (upperlowerRegex.findall(text)):
		return print('Sorry your password doesn\'t contain both upper and lower case')

	#TODO: digit validator to check if the password contains digit or not
	digitRegex = re.compile(r'\d+')
	if not (digitRegex.findall(text)):
		return print('Your password must have atleast a digit or more')

	#else the password by user is a strong password
	else:
		return print('Congratulation, you have created a strong password:)')

#function calling to see if the password is strong or not
strongPasswordDetector(stringUser)

input('Enter any key to continue:)')
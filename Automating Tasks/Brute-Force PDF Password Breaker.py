#! python3

# Brute-Force PDF Password Breaker.py - will decrypt the PDF by trying 
# every possible English word until it finds one that works.

import PyPDF2

# open file 'dictionary.txt' and add all the vocabulary to a list named 'password_list'
dictionaryfile_object = open('dictionary.txt')
password_list = dictionaryfile_object.readlines()

# open the pdf on which brute-force attack is to be tried
pdf_reader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

# try brute-force attack on the pdf file with decrypt() method until success
item = 0
# each word on 'password_list' is used in brute-force attack
password = str.lower((str(password_list[item]))[:-1])

while not pdf_reader.decrypt(password):

	# increment item to read next word in 'password_list'
	if item != len(password_list):
		
		item += 1
		password = str.lower((str(password_list[item]))[:-1])
	
	# if the list is finished then we break the loop
	else:
		print('Sorry no password found :(')
		break

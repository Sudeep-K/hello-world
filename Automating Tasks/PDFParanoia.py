#! python3

# PDFParanoia.py -  a script that will go through every PDF in a folder 
# (and its subfolders) and encrypt the PDFsusing a password provided on 
# the command line.

import os, PyPDF2, sys

# read the password from the command line input
if len(sys.argv) > 1:
	password = sys.argv[1] 

password = 'sudeep'

# walk through each file of the current directory

for dirpath, foldernames, filenames in os.walk('.'):

	# create a new directory named 'encrypted'
	os.makedirs('encrypted', exist_ok=True)

	for filename in filenames:
		# if your file has 'pdf' as file format then encrypt the file
		if filename.endswith('.pdf'):
			# open the 'pdf' file and read the content
			pdf_writer = PyPDF2.PdfFileWriter()
			pdf_reader = PyPDF2.PdfFileReader(open(os.path.join(os.path.abspath(dirpath),filename), 'rb'))
			
			# read the content of pdf file and copy them to 'pdf_writer' object
			for page_num in range(pdf_reader.numPages):
				
				page_object = pdf_reader.getPage(page_num)
				pdf_writer.addPage(page_object)

			# encrypt the file using the user given password and save the pdf file
			pdf_writer.encrypt(password)
			encrypted_file_object = open('.\\encrypted\\' + filename[:-4] + '_encrypted.pdf', 'wb')
			pdf_writer.write(encrypted_file_object)
			encrypted_file_object.close()

# decrypt the pdf files and create a new decypted pdf file

for dirpath, foldernames, filenames in os.walk('.'):

	# create a new directory named 'decrypted'
	os.makedirs('decrypted', exist_ok=True)
	
	for filename in filenames:
		# open file with 'pdf' format
		if filename.endswith('_encrypted.pdf'):
			pdf_reader = PyPDF2.PdfFileReader(open(os.path.join(os.path.abspath(dirpath),filename), 'rb'))
			# if you file is encypted then decrypt it with the key provided by user
			if pdf_reader.isEncrypted == True:
				pdf_reader.decrypt(password)

				pdf_writer = PyPDF2.PdfFileWriter()
				for page_num in range(pdf_reader.numPages):
					# add the decrypted pdf to new pdf
					pdf_writer.addPage(pdf_reader.getPage(page_num))

				# save the decrypted pdf file
				decypted_file_object = open('.\\decrypted\\' + filename[:-14] + '_decrypted.pdf', 'wb')
				pdf_writer.write(decypted_file_object)
				decypted_file_object.close()

print('.Done')


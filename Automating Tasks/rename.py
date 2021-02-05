#! python3
'''
To add a prefix to the start of the filename, such as adding spam_ to
rename eggs.txt to spam_eggs.txt
'''
import os, shutil

#TODO:ask user for prefix
filename_prefix = input('Enter the prefix that you want to add:\n')

#TODO:list all the files from the directory and rename them with prefix added
for filenames in os.listdir('.'):
	#ignore 'rename.py' code file
	if filenames == 'rename.py':
		continue
	#add prefix to filename
	newfilename = filename_prefix + filenames
	abs_path = os.path.abspath('.')
	filename_path = os.path.join(abs_path, filenames)
	newfilename_path = os.path.join(abs_path, newfilename)
	#rename all the files using shutil module
	shutil.move(filename_path, newfilename_path)
	
#ignore
input('Enter \'ENTER\' to quit()')
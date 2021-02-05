#! python3
'''
To change filenames with European-style dates to American-style dates
'''

# renameDates.py - Renames filenames with European DD-MM-YYYY date format
# to American MM-DD-YYYY.

import re, os, shutil

#TODO:create regex to match european date format
dateRegex = re.compile(r'''^(.*?)	#before date text
	((0|1|2|3)?\d)-					#two digits date
	((0|1)?\d)-						#two digits month
	((19|20)?\d\d)					#four digits year
	(.*?)$							#after date text
	''', re.VERBOSE)

#TODO:match the regex to filename and rename the file to American date format
for filenames in os.listdir('.'):
	matched_object = dateRegex.search(filenames)
	#when matched object is None then continue
	if matched_object == None:
		continue
	#store all groups to variable if matched object returns True
	else:
		before_text = matched_object.group(1)
		date = matched_object.group(2)
		month = matched_object.group(4)
		year = matched_object.group(6)
		after_text = matched_object.group(8)

	#rename new file with American date format
	new_filename = before_text + month + '-' + date + '-' + year + after_text
	abspath = os.path.abspath('.')
	filename_path = os.path.join(abspath, filenames)
	new_filename_path = os.path.join(abspath, new_filename)
	#rename using shutil.move()
	shutil.move(filename_path, new_filename_path)
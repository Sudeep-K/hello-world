#! python3
'''
To remove the zeros from files such as spam0042.txt
'''

import re, os, shutil

#TODO:create regex to catch the zeros
zero_regex = re.compile(r'^(.*?)([0]{1,})(.*?)$')
#TODO:list all the files and match the regex and then remove the zeros
for filenames in os.listdir('.'):
	matched_object = zero_regex.search(filenames)

	#ignore if there is no matched regex in filename
	if matched_object == None:
		continue
	#rename filename excluding zeros if matched regex
	else:
		before_zeros = matched_object.group(1)
		after_zeros = matched_object.group(3)

	new_filename = before_zeros + after_zeros
	abspath = os.path.abspath('.')
	filename_path = os.path.join(abspath, filenames)
	newfilename_path = os.path.join(abspath, new_filename)

	#rename file with shutil.move()
	shutil.move(filename_path, newfilename_path)

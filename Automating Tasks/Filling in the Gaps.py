#! python3
'''
Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the numbering 
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
'''


import os, shutil, re

#create a empty list 'filename_digit' to list the digits in filename
filename_digit = []

#walk over each file to read digits on each filename and store then to 'filename_digit' list
for dirpath, dirnames, filenames in os.walk('.'):
	for filename in filenames:
		filename_regex = re.compile(r'^(.*?)([0]{1,})(\d{1,})(.*?)$')
		matched_object = filename_regex.search(filename)
		if matched_object == None:
			continue
		else:
			filename_digit.append(int(matched_object.group(3)))

#sort the 'filename_digit' list to 'filename_digit_sorted' list
filename_digit_sorted = sorted(filename_digit)
#create a list 'filled_gap_filename' from first digit of list 'filename_digit_sorted' to length of the list filling all the gaps within
filled_gap_filename = list(range(filename_digit_sorted[0],len(filename_digit_sorted) + 1))

#this variable stores the index that is used to rename the file with gaps filled
position = 0

#rename the filename with gaps filled using list 'filled_gap_filename'
for dirpath, dirnames, filenames in os.walk('.'):
	for filename in filenames:
		matched_object = filename_regex.search(filename)
		if matched_object == None:
			continue
		else:
			new_filename = matched_object.group(1) + matched_object.group(2) + str(filled_gap_filename[position]) + matched_object.group(4)
			#absolute path of original filename
			abspath_filename = os.path.join(dirpath, filename)
			#absolute path of new filename
			abs_new_filename = os.path.join(dirpath, new_filename)
			position +=1
			#use shutil.move() to rename the filename to new_filename
			shutil.move(abspath_filename,abs_new_filename)
			
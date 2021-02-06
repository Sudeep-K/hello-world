#!python 3
'''
Find the folder in a directory tree that has the greatest number of files
or the folder that uses the most disk space
'''

import os

#create empty dictionary to store the filesize for each folder
size_dict = {}

#walk over the directory using os.walk module
for dirpath, dirnames, filenames in os.walk('YOUR PATH'):
	#initiate file size with 'zero' bytes
	file_size = 0
	#walk over each file adding their individual file size to 'file_size' variable
	for filename in filenames:
		file_size = file_size + os.path.getsize(os.path.join(dirpath, filename))

	#store the summation final file size to 'size_dict' dictionary with directory path as 'key' and file size as 'value'
	size_dict[dirpath] = file_size


key_list = list(size_dict.keys())
value_list = list(size_dict.values())

#find the maximum file size and find it's position
max_file_size = max(value_list)
position = value_list.index(max_file_size)
#print the maximum filesize and the folder that contains it
print(key_list[position], max_file_size, sep='\t')

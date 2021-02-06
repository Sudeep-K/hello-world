#! python3
'''
Deleting Unneeded Files
Write a program that walks through a folder tree and searches for exceptionally large files or folders—say,
ones that have a file size of more than 100MB. (Remember, to get a file’s size, you can use os.path.getsize()
from the os module.) Print these files with their absolute path to the screen.
'''

import os, shutil, send2trash

source_path = input('Enter the source path.')

for dirpath, dirnames, filenames in os.walk(source_path):
	for filename in filenames:
		abspath = os.path.join(dirpath, filename)
		if os.path.getsize(abspath) > 100000000:
			#os.unlink(abspath)
			send2trash.send2trash(abspath)
			print(abspath)
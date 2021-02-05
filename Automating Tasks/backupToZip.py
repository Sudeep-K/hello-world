#! python3
'''
Walk a directory tree and archive just files with certain extensions, such
as .txt or .py, and nothing else
'''
import os, shutil, zipfile

#define function to archive files with certain extensions such as .txt or .py
def backuptozip(folder):

	#absolute path of the folder
	folder = os.path.abspath(folder)

	number = 1
	while True:
		#create zip file name and 'number' variable keeps track of zip file version
		zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipfilename):
			break
		number = number + 1

	#create zip file with above zip file name
	print('Creating %s...'%(zipfilename))	
	zipfile_object = zipfile.ZipFile(zipfilename, 'w')
	
	#walk over folders, subfolders and files using os.walk function
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files in %s...'%(foldername))
		zipfile_object.write(foldername)

		for filename in filenames:
			newBase = os.path.basename(foldername) + '_'
			#ignore the zip files
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue
			#archive only the file extension ending with '.py' or '.txt'
			elif filename.endswith('.py') or filename.endswith('.txt'):
				zipfile_object.write(os.path.join(foldername, filename))

	print('Done')

backuptozip('FOLDER NAME')

input('Enter \'ENTER\' to exit()')
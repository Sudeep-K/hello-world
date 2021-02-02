#! python3
'''
mcb.pyw - Saves and loads pieces of text to the clipboard.
Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
		 py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
		 py.exe mcb.pyw list - Loads all keywords to clipboard.
		 py.exe mcb.pyw delete <keyboard> - deletes keyword from shelve
		 py.exe mcb.pyw delete - deletes all keyword from shelve
'''


'''
import sys for reading command line input, pyperclip to copy and 
paste string from clipboard, shelve to store variable data to file for 
future use
'''
import sys, pyperclip, shelve

#open the shelve file 'mcb' and initiate mcbShelf object
mcbShelf = shelve.open('F:\\python\\mcb')

#if the command line input has 3 strings as input then
if len(sys.argv) == 3 :
	#if the input is 'save' then we save the clipboard string to the keyword
	if sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()
	#if the input is 'delete' then we delete the keyword from shelve file
	elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
		del mcbShelf[sys.argv[2]]

#if the command line input has 2 string as input then
elif len(sys.argv) == 2:
	#if the input is 'list' then we return list of keyword saved to shelve file
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	#if the input is <keyword> then we copy the value of keyword to clipboard
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	#if the input is just 'delete' then we delete all the keyword from shelve file 'mcb'
	elif sys.argv[1].lower() == 'delete':
		for i in list(mcbShelf.keys()):
			del mcbShelf[i]

#we close the mcbShelf object
mcbShelf.close()
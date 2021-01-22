#comma code
"""a function that takes a list value as an argument and returns a string
with all the items separated by comma and a space, with 'and' inserted before 
last item"""

def stringMutable(spamRef):
	newSpam = ''
	
	#iterating over the list spam
	for itemsIndex in range(len(spamRef)):
		#for all items except last add ,
		if(itemsIndex < len(spamRef) - 1):
			newSpam = newSpam + spamRef[itemsIndex] + ', '
		#similarly for last item add and before the item itself
		elif (itemsIndex == len(spamRef) - 1):
			newSpam = newSpam + 'and ' + spamRef[itemsIndex]
	#now return the newly formed arranged list
	return newSpam



spam = ['apples', 'bananas', 'tofu', 'cats']

print(stringMutable(spam))


#! python
'''
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file.
The program would find these occurrences and prompt the user to
replace them.
The results should be printed to the screen and saved to a new text file.
'''
import re

#textFile = input('Enter the name of path of your file:)')

#TODO: read the content of file
fileObject = open('F:\\python\\purre.txt')
text = fileObject.read()
fileObject.close()

#TODO: replace the occurences of word ADJECTIVE, NOUN, ADVERB, or VERB appearing in the text file.
adjective = input('Enter an adjective')
noun1 = input('Enter a noun')
verb = input('Enter a verb')
noun2 = input('Enter a noun')

#TODO: create regex to replace above occurences in text file
#replace occurence of adjective
text = re.sub(r'\b{}\b'.format('ADJECTIVE'), adjective, text)
#replace occurence of noun
text = re.sub(r'^(.*?)\b{}\b'.format('NOUN'), r'\1{}'.format(noun1), text)
#replace occurence of verb
text = re.sub(r'\b{}\b'.format('VERB'), verb, text)
#replace occurence of noun
text = re.sub(r'^(.*?)\b{}\b'.format('NOUN'), r'\1{}'.format(noun2), text)

#TODO: print result to the screen
print(text)

#TODO: save result to the file
fileObject = open('F:\\python\\textfile.txt', 'w')
fileObject.write(text)
fileObject.close()

input('Enter \'ENTER\' to exit (:')

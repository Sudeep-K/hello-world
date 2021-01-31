#! python3
#a program to print each element of the list in column with right justified :)

#list which is to be printed with each column right justified
tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

#creating list containing maximum character of element in each column
colWidth = [0] * len(tableData)

#filling list colWidth with maximum character in each column
for i in range(len(tableData)):
	maximus = 0
	for j in range(len(tableData[i])):
		if len(tableData[i][j]) > maximus:
			maximus = len(tableData[i][j])
			colWidth[i] = maximus

##
mainList = range(len(tableData))

#final step to print each column right justified looping over each element
for j in range(len(tableData[i])):
	for i in mainList:
		print(tableData[i][j].rjust(colWidth[i]), end=' ')
	print('\n', end='')

#to stop python program to 'quit' abruptly
input('enter any key to continue :)')

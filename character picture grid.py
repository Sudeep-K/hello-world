#Character Picture grid

'''
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

'''

#we have to print the given list 'grid' in above format

#we define a function to print in the desired format
def characterPictureGrid(changedGrid):
	#looping over each row
	for i in range(len(changedGrid[0])):
		for j in range(len(changedGrid)):
			#printing each row
			print(changedGrid[j][i], end='')
		print('\n')

#this is the list that we need to send to function as attribute
grid = [['.', '.', '.', '.', '.', '.'],
 		['.', 'O', 'O', '.', '.', '.'],
 		['O', 'O', 'O', 'O', '.', '.'],
 		['O', 'O', 'O', 'O', 'O', '.'],
 		['.', 'O', 'O', 'O', 'O', 'O'],
 		['O', 'O', 'O', 'O', 'O', '.'],
 		['O', 'O', 'O', 'O', '.', '.'],
 		['.', 'O', 'O', '.', '.', '.'],
 		['.', '.', '.', '.', '.', '.']]

#calling our function character picture grid
characterPictureGrid(grid)
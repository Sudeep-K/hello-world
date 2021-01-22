#the collaz sequence

#define function collatzseq for printing collatz sequence
def collatzSeq(number):

	#returns (number // 2) if number is even
	if number % 2 == 0:
		print( number // 2 )
		return  number // 2 
	#returns (3 * number + 1) if the number is odd
	elif number % 2 != 0:
		print( 3 * number + 1 )
		return 3 * number + 1

#asks the user to input an integer
print('Input a number')
inputNumber = int(input())

#it keeps calling collatz() on that number until the function returns the value 1
while (inputNumber != 1 and inputNumber != 0):
	inputNumber = collatzSeq(inputNumber)
	
#!/usr/bin/env checkio --domain=py run the-square-chest

# On the chest keypad is a grid of numbered dots.    The grid is comprised of a square shaped array of dots and contains lines    that connect some pairs of adjacent dots.    The answer to the code is the number of squares that are formed by these lines.    For example, in the figure shown below, there are 3 squares: 2 small squares and 1 medium square.
# 
# 
# 
# The dots are marked by the numbers 1 through 16. The endpoints of the lines are represented by lists of two numbers.
# 
# Input:A list of lines as a list of list. Each list consists of the two integers.Output:The quantity of squares formed as an integer.
# END_DESC

from typing import List
def checkio(lines: List[List[int]]) -> int:
	#sort lines for comparison
	for line in lines:
		line.sort()

	#variables
	count=0
	allSquares=[]
	grid=[[ 1, 2, 3, 4], 
		  [ 5, 6, 7, 8], 
		  [ 9,10,11,12],
		  [13,14,15,16]]

	#find all possible squares
	for i in [i[0]-1 for i in grid[0:-1]]:
		for p in range(1,4):
			p=p+i
			allSquares.append([[p,p+1],[p+1,p+5],[p+4,p+5],[p,p+4]])

	for i in [i[0]-1 for i in grid[0:-2]]:
		for p in range(1,3):
			p=p+i
			allSquares.append([[p,p+1],[p+1,p+2],[p+2,p+6],[p+6,p+10],[p+9,p+10],[p+8,p+9],[p+4,p+8],[p,p+4]])

	allSquares.append([ [1,2],[2,3],[3,4],[1,5],[4,8],[5,9],[8,12],[9,13],[12,16],[13,14],[14,15],[15,16] ])

	#count squares in lines to check
	for square in allSquares:
		if all(line in lines for line in square):
			count=count+1

	return count



# '''
if __name__ == '__main__':
	print("Example:")
	print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
				   [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
				   [10, 14], [12, 16], [14, 15], [15, 16]]))

	assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
					 [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
					 [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
	assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
					 [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
					 [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
	assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
	assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
	assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
					 [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
	print("Coding complete? Click 'Check' to earn cool rewards!")
# '''
#!/usr/bin/env checkio --domain=py run can-pass

# If you have solved the"How to find friends"mission, then you already know how to check for the existence of a path    in graphs. Let's try to add something more to that problem.
# 
# You are given a matrix (2D array) and the coordinates (row and column) of two cells with the same value. The matrix    consists of digits. You may move to neighbouring cells either horizontally or vertically provided the values of the    origin and destination cells are equal. You should determine if a path exists between two given cells.
# 
# A matrix is represented as a tuple of tuples with digits. Coordinates are represented as a tuple with two numbers:    row and column. The result should be any value which can be converted into a boolean. If a path exists, then return    True. Return False if there is none.
# 
# 
# 
# Input:Three arguments. A matrix as a tuple of tuples with integers,    first and second cell coordinates as tuples of two integers.
# 
# Output:The existence of a path between two given cells    as a boolean or a value that can be converted to boolean.
# 
# Precondition:
# 1 < len(matrix) ≤ 10
# all(1 < len(row) ≤ 10 for row in matrix)
# all(all(0 ≤ x < 10 for x in row) for row in matrix)
# matrix[first[0]][first[1]] == matrix[second[0]][second[1]]
# first != second
# 
# 
# END_DESC

def explore(matrix,start,end,hard_path=True):
	y,x=start
	yE,xE=end
	soft_path=hard_path
	
	if y==end[0] and x==end[1]:
		return True

	matrix[y][x]=1
	if matrix[y][x+1]==matrix[yE][xE]:
		soft_path=explore(matrix,(y,x+1),end,hard_path)
		if soft_path!=False:
			return soft_path
	if matrix[y+1][x]==matrix[yE][xE]:
		soft_path=explore(matrix,(y+1,x),end,hard_path)
		if soft_path!=False:
			return soft_path
	if matrix[y][x-1]==matrix[yE][xE]:
		soft_path=explore(matrix,(y,x-1),end,hard_path)
		if soft_path!=False:
			return soft_path
	if matrix[y-1][x]==matrix[yE][xE]:
		soft_path=explore(matrix,(y-1,x),end,hard_path)
		if soft_path!=False:
			return soft_path
	return False

def can_pass(matrix, first, second):
	pad=1
	matrix=[list(l) for l in matrix]
	matrix=[[pad for i in range(len(matrix[0])+pad)]]+\
		   [[pad]+l+[pad] for l in matrix]+\
		   [[pad for i in range(len(matrix[0])+pad)]]
	fy,fx=first
	sy,sx=second
	return explore(matrix,(fy+1,fx+1),(sy+1,sx+1))

if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
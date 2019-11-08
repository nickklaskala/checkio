#!/usr/bin/env checkio --domain=py run x-o-referee

# def checkio(pos) -> str:
# 	t,m,b  ,l,c,r  ,winner=0,1,2  ,0,1,2  ,'D'
# 	for turn in 'XO':
# 		if any((
# 			all((pos[t][l]==turn,pos[t][m]==turn,pos[t][r]==turn)),
# 			all((pos[m][l]==turn, pos[m][c]==turn, pos[m][r]==turn)),
# 			all((pos[b][l]==turn, pos[b][c]==turn, pos[b][r]==turn)),
# 			all((pos[t][l]==turn, pos[m][l]==turn, pos[b][l]==turn)),
# 			all((pos[t][c]==turn, pos[m][c]==turn, pos[b][c]==turn)),
# 			all((pos[t][r]==turn, pos[m][r]==turn, pos[b][r]==turn)),
# 			all((pos[t][l]==turn, pos[m][c]==turn, pos[b][r]==turn)),
# 			all((pos[t][r]==turn, pos[m][c]==turn, pos[b][l]==turn))    )):
# 			winner=turn
# 	return winner

def checkio(pos) -> str:
	pos= "".join(pos)
	winner='D'
	checks = [ [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] ]
	for c in checks:
		for turn in 'XO':
			if all((pos[c[0]]==turn,pos[c[1]]==turn,pos[c[2]]==turn)):
				winner=turn
	return winner








# '''
if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio([
		"X.O",
		"XX.",
		"XOO"]) == "X", "Xs wins"
	assert checkio([
		"OO.",
		"XOX",
		"XOX"]) == "O", "Os wins"
	assert checkio([
		"OOX",
		"XXO",
		"OXX"]) == "D", "Draw"
	assert checkio([
		"O.X",
		"XX.",
		"XOO"]) == "X", "Xs wins again"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
# '''
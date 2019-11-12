#!/usr/bin/env checkio --domain=py run cipher-map2

# 
# END_DESC

def recall_password(cipher, password):
	psw=''
	cipher= [[c for c in l] for l in cipher]

	def flipGrid(grid):
		box=[[] for i in grid]
		for x in range(len(grid)):
			for y in range(len(grid)):
				box[y].append(grid[~x][y])
		return box

	for turn in range(len(password)):
		for l in range(len(cipher)):
			for c in range(len(cipher)):
				if cipher[l][c]=='X':
					psw+=password[l][c]
		cipher=flipGrid(cipher)

	print(psw)
	return psw


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert recall_password(
		('X...',
		 '..X.',
		 'X..X',
		 '....'),
		('itdf',
		 'gdce',
		 'aton',
		 'qrdi')) == 'icantforgetiddqd', 'First example'

	assert recall_password(
		('....',
		 'X..X',
		 '.X..',
		 '...X'),
		('xhwc',
		 'rsqx',
		 'xqzz',
		 'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

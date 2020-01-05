
# 
# END_DESC
def recall_password(grille, password):
	g = [[c for c in l] for l in grille]
	c = [[c for c in l] for l in password]
	pw=[]
	for i in range(4):
		pw.extend([[g,c] for g,c in zip(g,c) for g,c in zip(g,c)])
		g=[[g[~x][y] for x in range(len(g))] for y in range(len(g))]
	return ''.join([i[1] for i in pw if i[0]=='X'])

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

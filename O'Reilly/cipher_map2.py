#!/usr/bin/env checkio --domain=py run cipher-map2

# 
# END_DESC

def recall_password(cipher_grille, ciphered_password):
	



	return ""

cipher_grille, ciphered_password=('X...', '..X.', 'X..X', '....'), ('itdf', 'gdce', 'aton', 'qrdi')

cipher_grille, ciphered_password=('....', 'X..X', '.X..', '...X'), ('xhwc', 'rsqx', 'xqzz', 'fyzr')


cipher_grille=''.join(list(cipher_grille))
ciphered_password=''.join(list(ciphered_password))
psw=''

for i in range(len(cipher_grille)):
	if cipher_grille[i]=='X':
		psw+=ciphered_password[i]
print(psw)





'''
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
'''
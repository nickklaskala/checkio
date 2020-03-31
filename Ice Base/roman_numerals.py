#!/usr/bin/env checkio --domain=py run roman-numerals

# .numeral-table {    margin: auto;    border-collapse: collapse;    text-align: center;  }  .numeral-table * {    border: 1px solid black;    padding: 8px;    width: 50%;  }
# END_DESC

def checkio(data):
	numerals={'M':1000, 'C':100, 'X':10, 'I':1}
	rst=''
	for k,v in numerals.items():
		while data>=v and data-v>=0:
			rst+=k
			data=data-v

	rst=rst.replace('C'*9,'CM').replace('C'*5,'D').replace('C'*4,'CD')\
		   .replace('X'*9,'XC').replace('X'*5,'L').replace('X'*4,'XL')\
		   .replace('I'*9,'IX').replace('I'*5,'V').replace('I'*4,'IV')
	print(rst)

	return rst


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(6) == 'VI', '6'
	assert checkio(76) == 'LXXVI', '76'
	assert checkio(499) == 'CDXCIX', '499'
	assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
	print('Done! Go Check!')
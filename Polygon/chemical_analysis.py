#!/usr/bin/env checkio --domain=py run chemical-analysis

# As the input you will get the chemical formula and the number N. 
# Your task is to create a list of the chemical elements, which are in the formula in the amount of >= N.
# Pay attention, that in the some formulas will be used brackets - () and [].
# This articlewill help you to open the brackets and don't make mistake while counting.
# 
# Input:Chemical formula and the number of atoms.
# 
# Output:List of the chemical elements, sorted in the alphabetical order.
# 
# Precondition:
# 1<= different elements<= 10
# 
# END_DESC
def atoms(formula, limit):
	import re
	formula=re.findall(r'([A-Z][a-z]*|\W|\d)', formula)
	rst=''
	for c in formula:
		if c in ('(['):
			rst+='+( '
		elif c in (')]'):
			rst+=') '
		elif c.isdigit():
			rst+='*'+c+' '
		else:
			rst+="+'"+c+"'+"
	rst=eval(rst.replace('+*','*').replace('++','+').replace('( +','(').replace('+)',')')[1:-1])

	rst=re.findall(r'([A-Z][a-z]*|\W|\d)', rst)
	rst=[c for c in sorted(set(rst)) if rst.count(c)>=limit]
	return rst


if __name__ == '__main__':
	print("Example:")
	assert atoms('Mg(OH)2', 1) == ['H', 'Mg', 'O']
	print(atoms('C2H5OH', 2))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert atoms('C2H5OH', 2) == ['C', 'H']
	assert atoms('H2O', 2) == ['H']
	assert atoms('K4[ON(SO3)2]2', 4) == ['K', 'O', 'S']
	print("Coding complete? Click 'Check' to earn cool rewards!")


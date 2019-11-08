#!/usr/bin/env checkio --domain=py run completely-empty

def completely_empty(val):
	print(val)
	if len(str(val))==0:
		return True
	elif type(val)==dict:
		if not all(completely_empty(k) for k,v in val.items()) :
			print('Falsedict')
			return False
		else:
			print('trueDict')
			return True
	elif type(val)==list:
		if not all(completely_empty(v) for v in val) :
			print('Falselist')
			return False
		else:
			print('trueList')
			return True
	elif len(str(val))>0:
		print('falseVal')
		return False
	else:
		print('truVal')
		return True

completely_empty([iter(())])

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert completely_empty([]) == True, "First"
	assert completely_empty([1]) == False, "Second"
	assert completely_empty([[]]) == True, "Third"
	assert completely_empty([[],[]]) == True, "Forth"
	assert completely_empty([[[]]]) == True, "Fifth"
	assert completely_empty([[],[1]]) == False, "Sixth"
	assert completely_empty(['']) == True
	assert completely_empty([0]) == False, "[0]"
	assert completely_empty([[],[{'':'No WAY'}]]) == True
	print('Done')

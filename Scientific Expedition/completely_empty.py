#!/usr/bin/env checkio --domain=py run completely-empty

def test(val):
	test(val)
def completely_empty(iterable):
	try:
		return all(completely_empty(i) for i in iterable)
	except:
		return False






# completely_empty([0])
# x=completely_empty(['3'])
# print (x)


# def func(val):
# 	val+1
# x=[]

# def func2(val):
# 	try:
# 		print('hi')
# 		func(val)
# 	except:
# 		print('except')

# v=func2(x)
# print(v)





if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert completely_empty(['']) == True
	assert completely_empty([]) == True, "First"
	assert completely_empty([1]) == False, "Second"
	assert completely_empty([[]]) == True, "Third"
	assert completely_empty([[],[]]) == True, "Forth"
	assert completely_empty([[[]]]) == True, "Fifth"
	assert completely_empty([[],[1]]) == False, "Sixth"
	assert completely_empty([0]) == False, "[0]"
	assert completely_empty([[],[{'':'No WAY'}]]) == True
	print('Done')

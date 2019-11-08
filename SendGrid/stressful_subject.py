#!/usr/bin/env checkio --domain=py run stressful-subject

# 
# END_DESC
import re
def is_stressful(subj):
    exp=re.compile(r'(h+\W*e+\W*l+\W*p+|a+\W*s+\W*a+\W*p+|u\W*r+\W*g+\W*e+\W*n+\W*t+)')
	if subj.isupper()==True or subj.endswith('!!!') or exp.search(subj.lower()):
		return True
	return False





# '''
if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert is_stressful("Hi") == False, "First"
	assert is_stressful("I neeed HELP") == True, "Second"
	assert is_stressful("hello puppy") == False, "Second"
	print('Done! Go Check it!')
# '''
#!/usr/bin/env checkio --domain=py run flatten-list

# 
# END_DESC

def flat_list(x):
	ml=[]
	for i in x:
		if type(i)==list:
			ml.extend(flat_list(i))
		else:
			ml.append(i)
	return ml

if __name__ == '__main__':
	assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
	assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
	assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
	assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
	print('Done! Check it')
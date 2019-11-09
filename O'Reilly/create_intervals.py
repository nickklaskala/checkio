#!/usr/bin/env checkio --domain=py run create-intervals


def create_intervals(data):
	l=sorted(x for x in data if x-1 not in data)
	r=sorted(x for x in data if x+1 not in data)
	return list(zip(l,r))



if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
	assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
	assert create_intervals([]) == [], "Second"
	print('Almost done! The only thing left to do is to Check it!')
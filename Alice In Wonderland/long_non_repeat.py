#!/usr/bin/env checkio --domain=py run long-non-repeat

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# A very similar to the first is the second mission of the series with only one distinction is that you should look in a completely different way. You need to find the first longest substring with all unique letters. For example, in substring "abca" we have two substrings with unique letters "abc" and "bca", but we should take the first one, so the answer is "abc".
# 
# Input:String.Output:String.
# 
# 
# 
# 
# END_DESC

#letters "abc" and "bca", but we should take the first one, so the answer is "abc".






def non_repeat(line):
	dct,w={0:''},0
	for l in line:
		if l in dct[w]:
			w+=1
			p=dct[w-1].find(l)+1
			dct[w]=dct[w-1][p:]
		dct[w]+=l
	return max(dct.values(), key=len)


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert non_repeat('aaaaa') == 'a', "First"
	assert non_repeat('abdjwawk') == 'abdjw', "Second"
	assert non_repeat('abcabcffab') == 'abcf', "Third"
	print('"Run" is good. How is "Check"?')
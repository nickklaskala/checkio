#!/usr/bin/env checkio --domain=py run the-longest-palindromic

# Write a function that finds the longestpalindromicsubstring of a given string. Try to be as efficient as possible!
# 
# If you find more than one substring, you should return the one that’s closer to the beginning.
# 
# Input:A text as a string.
# 
# Output:The longest palindromic substring.
# 
# Precondition:1<|text| ≤ 20
# The text contains only ASCII characters.
# 
# 
# END_DESC

from itertools import product

def longest_palindromic(line):
	line=''.join(reversed(line))
	k=range(len(line)+1)
	longest=''
	
	for h,g in product(k,k):
		text=line[g:h]
		if  all([text[i]==text[~i] for i in range(len(text)//2)]) and len(text)>=len(longest):
			longest=text

	return longest


if __name__ == '__main__':
	print("Example:")
	print(longest_palindromic('abc'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert longest_palindromic('abc') == 'a'
	assert longest_palindromic('abacada') == 'aba'
	assert longest_palindromic('artrartrt') == 'rtrartr'
	assert longest_palindromic('Codingcomplete?ClickChecktoearncoolrewards!!sdrawerloocnraeotkcehCkcilC?etelpmocgnidoC')=='Codingcomplete?ClickChecktoearncoolrewards!!sdrawerloocnraeotkcehCkcilC?etelpmocgnidoC'
	print("Coding complete? Click 'Check' to earn cool rewards!")
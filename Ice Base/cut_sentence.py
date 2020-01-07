#!/usr/bin/env checkio --domain=py run cut-sentence

# Your task in this mission is to truncate a sentence to a length, that does not exceed a  given number of characters.
# 
# If the given sentence already is short enough you don't have to do anything to it, but  if it needs to be truncated the omission must be indicated by concatenating an ellipsis  ("...") to the end of the shortened sentence.
# 
# The shortened sentence can contain complete words and spaces.
# It must neither contain truncated words nor trailing spaces.
# The ellipsis has been taken into account for the allowed number of characters, so it  does not count against the given length.
# 
# Input:Two arguments:one-line sentence as a stringmax length of the truncated sentence as an int
# 
# Output:The shortened sentence plus the ellipsis (if required) as a  one-line string.
# 
# Precondition:
# line.startswith(' ') == False0<len(line) ≤ 790<length ≤ 76all(char in string.ascii_letters + ' ' for char in line)
# 
# 
# END_DESC





def cut(line, length):
	indexes=[i for i in range(len(line)) if line[i]==' ']+[len(line)]
	rst=line
	for loc in reversed(indexes):
		rst=line[:loc]+'...'
		if loc<=length:
			break
	return rst[:len(line)]



if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert cut("Hi my name is Alex", 4) == "Hi...", "First"
	assert cut("Hi my name is Alex", 8) == "Hi my...", "Second"
	assert cut("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
	assert cut("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
	print('Done! Do you like it? Go Check it!')
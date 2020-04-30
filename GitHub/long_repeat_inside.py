#!/usr/bin/env checkio --domain=py run long-repeat-inside

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# It is the fourth and the last mission of the series. But if in the first mission you needed to find repeating letters, then in this one you should find a repeating sequence inside the substring. I have an example for you: in a string "abababc" - "ab" is a sequence that repeats more than once, so the answer will be "ababab"
# 
# Input:String.Output:String.
# 
# 
# END_DESC

def repeat_inside(string):
    from itertools import product
    result = ''
    for i, j, k in product(range(len(string)),  range(len(string)), range(len(string))):     
       pattern = string[i:j]*(k+2)
       if pattern in string:
           result = max(result, pattern, key=len)
    return result 



# def repeat_inside(line):
# 	dct={1:''}
# 	count=1
# 	for i in range(int(len(line)/2)):
# 		for z in range(len(line)-i):
# 			temp=[line[l:l+i+1] for l in range(z,len(line)-i,i+1)]
# 			for t in range(len(temp)-1):
# 				if temp[t]==temp[t+1] and dct[count]=='':
# 					dct[count]=temp[t]+temp[t]
# 				elif temp[t]==temp[t+1]:
# 					dct[count]+=temp[t]
# 				else:
# 					count+=1
# 					dct[count]=''
# 			count+=1
# 			dct[count]=''
# 	# print(dct)
# 	return max(dct.values(),key=len)


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert repeat_inside('aaaaa') == 'aaaaa', "First"
	assert repeat_inside('aabbff') == 'aa', "Second"
	assert repeat_inside('aababcc') == 'abab', "Third"
	assert repeat_inside('abc') == '', "Forth"
	assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
	print('"Run" is good. How is "Check"?')
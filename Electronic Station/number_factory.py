#!/usr/bin/env checkio --domain=py run number-factory

# You are given a two or more digits numberN.
# For this mission, you should find the smallest positive number ofX,
# such that the product of its digits is equal to N.
# If X does not exist, then return 0.
# 
# Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit.
# Also we can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.
# 
# Hints:Remember prime numbers (numbers divisible by only one) and be careful with endless loops.
# 
# Input:A number N as an integer.
# 
# Output:The number X as an integer.
# 
# How it is used:This task will teach you how to work with numbers in code.
# You can factorize numbers and reconstruct them into new numbers.
# Of course you can solve this problem with brute force,
# but is that the best way?
# Numbers are the foundation of mathematics and programming.
# 
# Precondition:
# 9 < N < 105.
# 
# 
# END_DESC

def checkio(num):

    from itertools import product
	p=[1,2,3,5,7]
	factors=[0]
	for j,k,l,m,n,o,p,q,r,s in product(p,p,p,p,p,p,p,p,p,p):
		if j*k*l*m*n*o*p*q*r*s==num:
			factors+=sorted([j,k,l,m,n,o,p,q,r,s])
			while 1 in factors:
				factors.remove(1)
			while 0 in factors:
				factors.remove(0)
			break

	while factors.count(2)>=3:
		factors.remove(2)
		factors.remove(2)
		factors.remove(2)
		factors.append(8)
    
    while factors.count(3)>1:
		factors.remove(3)
		factors.remove(3)
		factors.append(9)

	while factors.count(3)>0 and factors.count(2)>0:
		factors.remove(2)
		factors.remove(3)
		factors.append(6)

	while factors.count(2)>1:
		factors.remove(2)
		factors.remove(2)
		factors.append(4)




	factors.sort()
	x=int(''.join(map(str,factors)))
	return x




if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(20) == 45, "1st example"
	assert checkio(21) == 37, "2nd example"
	assert checkio(17) == 0, "3rd example"
	assert checkio(33) == 0, "4th example"
	assert checkio(3125) == 55555, "5th example"
	assert checkio(9973) == 0, "6th example"
#!/usr/bin/env checkio --domain=py run friendly-number

# 
# END_DESC

def friendly_number(number, base=1000, decimals=0, suffix='',powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    counter=0
	while abs(number)>=base and counter+1<len(powers):
		number=round(number/base,1)
		counter+=1
	if decimals==0:
		number=int(number)
	print("{:.{}f}".format( number, decimals )+powers[counter]+suffix)
	return "{:.{}f}".format( number, decimals )+powers[counter]+suffix



friendly_number(102)
friendly_number(10240)
friendly_number(12341234, decimals=1)
friendly_number(12461, decimals=1)
friendly_number(1024000000, base=1024, suffix='iB')
friendly_number(255000000000, powers=["","k","M"])
friendly_number(10**24)#1Y
friendly_number(10**32)#Right result:"100000000Y"


number=10**32
base=1000
decimals=0
suffix=''
powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
counter=0
while abs(number)>=base and counter+1<len(powers):
	number=round(number/base,1)
	print(number)
	counter+=1
if decimals==0:
	number=int(number)
print("{:.{}f}".format( number, decimals )+powers[counter]+suffix)





'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert friendly_number(102) == '102', '102'
	assert friendly_number(10240) == '10k', '10k'
	assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
	assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
	assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

'''
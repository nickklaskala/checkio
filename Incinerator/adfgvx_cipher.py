#!/usr/bin/env checkio --domain=py run adfgvx-cipher

# TheADFGVX Cipherwas a field cipher used by the German Army on the Western Front during World War I.    ADFGVX was in fact an extension of an earlier cipher called ADFGX.    Invented by Colonel Fritz Nebel and introduced in March 1918, the cipher was a fractionating transposition cipher    which combined a modified Polybius square with a single columnar transposition.    The cipher is named after the six possible letters used in the ciphertext:    A, D, F, G, V and X. These letters were chosen deliberately    because they sound very different from each other when transmitted via Morse code.    The intention was to reduce the possibility of operator error.
# 
# Let's examine the way cipher works using an example. Our message is "I am going." First we must clean and process    the message: "iamgoing". It should contain only digits and latin letters in lowercase. All other characters (such as    punctuation) are skipped. Then we fill the "adfgvx" table with our secret alphabet    "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g".
# 
# 
# \  A D F G V X
#  \------------
# A| d h x m u 4
# D| p 3 j 6 a o
# F| i b z v 9 w
# G| 1 n 7 0 q k
# V| f s l y c 8
# X| t r 5 e 2 g
# 
# Using this square, the message is converted to fractionated form (row-column):
# 
# 
# i  a  m  g  o  i  n  g
# FA DV AG XX DX FA GD XX
# 
# Then, a new table is created with a key as the heading. Let's use 'cipher' as the key.If the key contains duplicated letters, the first one should be used.So, "checkio" becomes "chekio".
# 
# 
# c i p h e r
# -----------
# F A D V A G
# X X D X F A
# G D X X
# 
# The columns are sorted alphabetically based on the keyword and the table changes to the new form.
# 
# 
# c e h i p r
# -----------
# F A V A D G
# X F X X D A
# G   X D X
# 
# Then it is read off in columns, in keyword order and the result is "FXGAFVXXAXDDDXGA".
# 
# You should write two functions - "encode" and "decode". Each function receives a message (ciphered or opened),    a secret alphabet and a keyword.    The "encode" function processes and encrypts a message. The "decode" function decrypts the encoded message    (of course in the processed version).
# 
# Input:Three arguments. A message, a secret alphabet and a keyword as strings.
# 
# Output:The processed message as a string.
# 
# Precondition:
# re.match("[a-z]+\Z", keyword)
# re.match("[a-z0-9]+\Z", secret_alphabet)
# len(set(secret_alphabet)) == len(secret_alphabet)
# 
# 
# 
# END_DESC

def encode(message, secret_alphabet, keyword):

	message=message.replace(' ','').replace(':','').lower()
	headers='ADFGVX'

	encodedmessage=[(divmod(secret_alphabet.index(i),len(headers))) for i in message]
	encodedmessage=[headers[value] for subset in encodedmessage for value in subset]

	mydct={l:[] for l in set(keyword)}
	newkey=[]
	[newkey.append(l) for l in keyword if l not in newkey]

	for l in newkey*10000:
		if len(encodedmessage)==0:
			break
		mydct[l].append(encodedmessage[0])
		encodedmessage.pop(0)

	rst=[]
	[rst.extend(mydct[k]) for k in list(sorted([k for k,v in mydct.items()]))]

	return ''.join(rst)


def decode(message, secret_alphabet, keyword):
	headers='ADFGVX'
	newkey=[]
	[newkey.append(l) for l in keyword if l not in newkey]
	messageTemp=[l for l in message]
	mydct={l:[] for l in set(keyword)}
	for l in newkey*10000:
		if len(messageTemp)==0:
			break
		mydct[l].append(messageTemp[0])
		messageTemp.pop(0)
	for k,v in mydct.items():
		mydct[k]=len(v)
	mydct2={l:[] for l in set(keyword)}
	messageTemp=[l for l in message]

	for l in sorted(newkey):
		for i in range(0,mydct[l]):
			mydct2[l].append(messageTemp[0])
			messageTemp.pop(0)

	messageTemp=[l for l in message]
	mylist=[]
	for l in newkey*10000:
		if len(messageTemp)==0:
			break
		mylist.append(mydct2[l][0])
		mydct2[l].pop(0)
		messageTemp.pop(0)
	# mymap=[divmod(secret_alphabet.index(i),5) for i in mylist]
	rstTemp=[]
	for i in range(0,int(len(message)/2)):
		rstTemp.append(headers.index(mylist[0])*len(headers)+headers.index(mylist[1]))
		


		mylist.pop(0)
		mylist.pop(0)
	rst=''.join([secret_alphabet[i] for i in rstTemp])
	return rst





if __name__ == '__main__':
	assert encode("I am going", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g","weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
	assert encode("I am going", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g","cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
	assert encode("ditiszeergeheim", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz","piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
	assert encode("attack at 12:00 am", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz","privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
	assert decode("FXGAFVXXAXDDDXGA", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g","cipher") == 'iamgoing', "decode I am going"
	assert decode("DXGAXAAXXVDDFGFX", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g","weasel") == 'iamgoing', "decode weasel == weasl"
	assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz","privacy") == 'attackat1200am', "decode attack"
	assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz","piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
def checkio(numbers):
	routes=[]
	network={i:[n for n in numbers if  sum(map(lambda a,b:a==b,str(i),str(n)))==2] for i in numbers}

	def probe(path):
		if path[-1]==numbers[-1]:
			routes.append(path)
		for node in list(set(network[path[-1]])-set(path)):
			probe(path+[node])

	probe(numbers[0:1])
	return min(routes,key=len)



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
	assert checkio([555,545])==[555,545],'bingo'
	assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
	assert checkio([456, 455, 454, 356, 656, 654]) in ([456, 454, 654],[456, 656, 654])," is correct too"
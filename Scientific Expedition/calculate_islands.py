def checkio(map):
	#i padded the map with a zero so i dont have to get funky cheking points on borders, this way i know no border has a 1 and all checks for points previously on border will be valid indexes
	map=[[0 for i in range(len(map[0])+2)]]+\
		[[0]+l+[0] for l in map]+\
		[[0 for i in range(len(map[0])+2)]]
	island=0
	dct={}

	def probe(map,y,x,island):
		if island not in dct:
			dct[island]=[(y,x)]
		coords=[(y+1,x),(y+1,x+1),(y,x+1),(y-1,x+1),(y-1,x),(y-1,x-1),(y,x-1),(y+1,x-1)]#static
		for coord in coords:
			y,x=coord
			if map[y][x]==1 and coord not in dct[island]:
				dct[island].append(coord)
				probe(map,y,x,island)

	for y in range(len(map)):
		for x in range(len(map[0])):
			if map[y][x]==1:
				if not any((y,x) in v for v in dct.values()):
					island+=1
					probe(map,y,x,island)

	return sorted([len(v) for v in dct.values()])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	print("Example:")
	print(checkio([[0, 0, 0, 0, 0],
				   [0, 0, 1, 1, 0],
				   [0, 0, 0, 1, 0],
				   [0, 1, 0, 0, 0],
				   [0, 0, 0, 0, 0]]))

	assert checkio([[0, 0, 0, 0, 0],
					[0, 0, 1, 1, 0],
					[0, 0, 0, 1, 0],
					[0, 1, 0, 0, 0],
					[0, 0, 0, 0, 0]]) == [1, 3], "1st example"
	assert checkio([[0, 0, 0, 0, 0],
					[0, 0, 1, 1, 0],
					[0, 0, 0, 1, 0],
					[0, 1, 1, 0, 0]]) == [5], "2nd example"
	assert checkio([[0, 0, 0, 0, 0, 0],
					[1, 0, 0, 1, 1, 1],
					[1, 0, 0, 0, 0, 0],
					[0, 0, 1, 1, 1, 0],
					[0, 0, 0, 0, 0, 0],
					[0, 1, 1, 1, 1, 0],
					[0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
	print("Coding complete? Click 'Check' to earn cool rewards!")

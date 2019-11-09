#!/usr/bin/env checkio --domain=py run calculate-islands

# The Robots have found a chain of islands in the middle of the Ocean.    They would like to explore these islands and have asked for your help calculating the areas of each island.    They have given you a map of the territory. The map is a 2D array, where 0 is water, 1 is land.    An island is a group of land cells surround by water.    Cells are connected by their edges and corners.    You should calculate the areas for each of the islands and return a list of sizes (quantity of cells) in    ascending order.    All of the cells outside the map are considered to be water.
# 
# 
# 
# Input:A map as a list of lists with 1 or 0.
# 
# Output:The sizes of island as a list of integers.
# 
# Precondition:0 < len(land_map) < 10
# all(len(land_map[0]) == len(row) for row in land_map)
# any(any(row) for row in land_map)
# 
# 
# END_DESC

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
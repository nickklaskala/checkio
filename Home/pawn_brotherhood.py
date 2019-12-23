#!/usr/bin/env checkio --domain=py run pawn-brotherhood
# 
# END_DESC

def safe_pawns(pawns: set) -> int:

	pawns_indexes = [(int(p[1])-1,ord(p[0])-97) for p in pawns]
	count = 0
	for row, col in pawns_indexes:
		is_safe = (row-1,col+1) in pawns_indexes or (row-1,col-1) in pawns_indexes
		if is_safe:
			count += 1
	return count



if __name__ == '__main__':
	assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
	assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

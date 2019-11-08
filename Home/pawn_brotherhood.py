#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# 
# END_DESC

def safe_pawns(pawns: set) -> int:





	return 0




pawns={"b4", "d4", "f4", "c3", "e3", "g5", "d2"}


pawns_indexes = set()
for p in pawns:
	row = int(p[1]) - 1
	col = ord(p[0]) - 97
	pawns_indexes.add((row, col))
print(pawns_indexes)

count = 0
for row, col in pawns_indexes:
	is_safe = True if (row-1,col+1) not in pawns_indexes and (row-1,col-1) else False
	if is_safe:
		count += 1

print(count)


# '''
if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
	assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
# 	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
# '''
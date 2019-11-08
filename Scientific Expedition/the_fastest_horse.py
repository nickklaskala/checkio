#!/usr/bin/env checkio --domain=py run the-fastest-horse

def fastest_horse(horses: list) -> int:
	winners=[race.index(min(race)) for race in horses if race.count(min(race))==1]
	mostFrequentWinner=max(winners,key=winners.count)+1
	return mostFrequentWinner



if __name__ == '__main__':
	print("Example:")
	print(fastest_horse([['1:13', '1:26', '1:11']]))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
	print("Coding complete? Click 'Check' to earn cool rewards!")


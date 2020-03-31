#!/usr/bin/env checkio --domain=py run disposable-teleports

# The island has eight stations which are connected by a network of teleports;    however, the teleports take a very long time to recharge.    This means you can only use each one once.    After you use a teleport, it will shut down and no longer function.    But you can visit any station more than once.    For this task, you should begin at number 1 and try to travel around to all the stations before returning to the starting point.     The map of the teleports is presented as a string in which the comma-separated list represents teleports.    Each teleport is given the name of the station it connects to. This name consists of two digits, such as '12' or '32.'    Each test requires you to provide a route which passes through every station.    A route is presented as a string of the station numbers in the sequence in which they must be visited    (ex. 123456781).
# 
# 
# 
# Input:A teleport map as a string.
# 
# Output:The sequence of station numbers as a string.
# 
# Precondition:
# len(stations) == 8
# Teleports are not repeated and undirected.
# 
# 
# END_DESC

def checkio(teleports_string,teleport='00',hardRoute='1'):
	softRoute=hardRoute
	network = teleports_string.split(',')
	if (softRoute[0],softRoute[-1])==('1','1') and all([l in softRoute for l in '12345678']):
		return softRoute
	if teleport in network:
		network.remove(teleport)
	for i in range(len(network)):
		teleport=network[i]
		if hardRoute[-1] in teleport:
			softRoute=checkio(','.join(network),teleport,hardRoute+teleport[~teleport.index(hardRoute[-1])])
			if softRoute!='Dead End':
				return softRoute
	return 'Dead End'


#This part is using only for self-testing
if __name__ == "__main__":
	def check_solution(func, teleports_str):
		route = func(teleports_str)
		teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
		if route[0] != '1' or route[-1] != '1':
			print("The path must start and end at 1")
			return False
		ch_route = route[0]
		for i in range(len(route) - 1):
			teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
			if not teleport in teleports_map:
				print("No way from {0} to {1}".format(route[i], route[i + 1]))
				return False
			teleports_map.remove(teleport)
			ch_route += route[i + 1]
		for s in range(1, 9):
			if not str(s) in ch_route:
				print("You forgot about {0}".format(s))
				return False
		return True

	assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
	assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
	assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
	assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"
#!/usr/bin/env checkio --domain=py run node-disconnected-users2
# 
# END_DESC
def disconnected_users(net, users, source, crushes):
	population=sum(users.values())
	aliveNodes=[source] if source not in crushes else []

	for k in users.keys():
		for subnet in net:
			if source in subnet or any(node in subnet for node in aliveNodes):
				if not any(crush in subnet for crush in crushes): 
					for node in subnet:
						if node not in aliveNodes:
							aliveNodes.append(node)

	pigeons=population-(sum(users[k] for k in aliveNodes))
	return pigeons






if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert disconnected_users([
		['A', 'B'],
		['B', 'C'],
		['C', 'D']
	], {
		'A': 10,
		'B': 20,
		'C': 30,
		'D': 40
	},
		'A', ['C']) == 70, "First"
	assert disconnected_users([
		['A', 'B'],
		['B', 'D'],
		['A', 'C'],
		['C', 'D']
	], {
		'A': 10,
		'B': 0,
		'C': 0,
		'D': 40
	},
		'A', ['B']) == 0, "Second"
	assert disconnected_users([
		['A', 'B'],
		['A', 'C'],
		['A', 'D'],
		['A', 'E'],
		['A', 'F']
	], {
		'A': 10,
		'B': 10,
		'C': 10,
		'D': 10,
		'E': 10,
		'F': 10
	},
		'C', ['A']) == 50, "Third"
	print('Done. Try to check now. There are a lot of other tests')
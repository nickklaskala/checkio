#!/usr/bin/env checkio --domain=py run the-warriors

# 
# END_DESC

class Warrior:
	health=50
	attack=5
	is_alive=True
	

class Knight(Warrior):
	attack=Warrior.attack+2
	


def fight(p1, p2):
	while p2.is_alive and p2.is_alive:
		p2.health-=p1.attack
		if p2.health<=0:
			p2.is_alive=False
			return True
		p1.health-=p2.attack
		if p1.health<=0:
			p1.is_alive=False
			return False



if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing

	chuck = Warrior()
	bruce = Warrior()

	carl = Knight()
	dave = Warrior()

	mark = Warrior()

	assert fight(chuck, bruce) == True
	assert chuck.is_alive == True
	assert bruce.is_alive == False

	assert fight(dave, carl) == False
	assert carl.is_alive == True
	assert dave.is_alive == False

	assert fight(carl, mark) == False
	assert carl.is_alive == False

	print("Coding complete? Let's try tests!")
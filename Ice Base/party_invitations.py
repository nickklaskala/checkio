#!/usr/bin/env checkio --domain=py run party-invitations

# Each week you are meeting with your friends to spend some quality time together. Usually you're hanging out in a bar on Friday nights, or going out of town on Saturdays, or playing the board games on Sundays. You want to simplify the process of gathering people and that's why you've decided to write a program which could automate this process.
# You should create the class Party(place) which will send the invites to all of your friends.Also you should create the class Friend and each friend will be an instance of this class.
# Sometimes the circle of friends is changing - new friends appear, the old ones disappear from your life (for example - move to another town). To form right connections you should create the Party class with the next methods:
# 
# add_friend(Friend(name)) - add friend 'name' to the list of the 'observers' (people, which will get the invitations, when the new party is scheduled).
# del_friend(friend) - remove 'friend' from the 'observers' list.
# send_invites()- send the invites with the right day and time to the each person on the list of 'observers'.
# Class Friend should have theshow_invite()method which returns the string with the last invite that the person has received with the right place, day and time. The right place - is the 'place' which is given to the Party instance in the moment of creation. If the person didn't get any invites, this method should return - "No party..."
# In this mission you could use theObserverdesign pattern.
# 
# Examples:
# party = Party("Midnight Pub")
# nick = Friend("Nick")
# john = Friend("John")
# lucy = Friend("Lucy")
# chuck = Friend("Chuck")
# 
# party.add_friend(nick)
# party.add_friend(john)
# party.add_friend(lucy)
# party.send_invites("Friday, 9:00 PM")
# party.del_friend(nick)
# party.send_invites("Saturday, 10:00 AM")
# party.add_friend(chuck)
# 
# john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
# lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
# nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
# chuck.show_invite() == "No party..."
# 
# 
# 
# Input:The Party class methods and friends.
# 
# Output:The text of the last invite received by a person.
# 
# Precondition:All friends' names will be different.
# 
# 
# END_DESC


# class Friend:
# 	def __init__(self, name):
# 		self.name = name
# 		self.message = 'No party...'

# 	def invite(self, message):
# 		self.message = message

# 	def show_invite(self):
# 		return self.message


# class Party:
# 	def __init__(self, place):
# 		self.place = place
# 		self.friends = []

# 	def add_friend(self, friend):
# 		self.friends.append(friend)
	
# 	def del_friend(self, friend):
# 		self.friends.remove(friend)

# 	def send_invites(self, date):
# 		for friend in self.friends:
# 			friend.invite(f'{self.place}: {date}')




# class Friend:
# 	def __init__(self,name):
# 		self.name=name

# 		self.invites='No party...'

# 	def show_invite(self):
# 		print(self.invites)
# 		return self.invites


# class Party:
# 	def __init__(self,name):
# 		self.name=name
# 		self.friends=[]

# 	def add_friend(self,friend):
# 		self.friends.append(friend)

# 	def del_friend(self,friend):
# 		self.friends.remove(friend)

# 	def send_invites(self,when):
# 		for friend in self.friends:
# 			friend.invites=self.name+': '+when


class Named:
    def __init__(self, name):
        self.name = name


class Friend(Named):
    invitation = 'No party...'

    def show_invite(self):
        return self.invitation


class Party(Named,list):
    add_friend, del_friend = list.append, list.remove
    
    def send_invites(self, time):
        for f in self: f.invitation = f'{self.name}: {time}'

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing

	party_1 = Party("Celentano")
	party_2 = Party("Itaka")
	party_3 = Party("Disneyland")
	john = Friend('John')
	rose = Friend('Rose')
	gabe = Friend('Gabe')
	party_1.add_friend(john)
	party_1.add_friend(john)
	party_1.add_friend(john)
	party_2.add_friend(rose)
	party_3.add_friend(gabe)
	rose.show_invite()
	for i in party_1:
		print(i)
	

	party_1.send_invites('Friday, 18:45')
	party_2.send_invites('Saturday, 12:30')
	party_3.send_invites('Sunday, 10:00')
	rose.show_invite()
	john.show_invite()
	gabe.show_invite()
	print("Coding complete? Let's try tests!")



	party = Party("Midnight Pub")
	nick = Friend("Nick")
	john = Friend("John")
	lucy = Friend("Lucy")
	chuck = Friend("Chuck")

	party.add_friend(nick)
	party.add_friend(john)
	party.add_friend(lucy)
	party.send_invites("Friday, 9:00 PM")
	party.del_friend(nick)
	party.send_invites("Saturday, 10:00 AM")
	party.add_friend(chuck)

	assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
	assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
	assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
	assert chuck.show_invite() == "No party..."
	print("Coding complete? Let's try tests!")
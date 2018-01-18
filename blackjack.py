#Blackjack

#Written by:	Jesus Bibieca
#Date:			Jan 14, 2018

import random as R

class Card(object):
	def __init__(self): #pending add the color
		self.color = ''
		self.number =  R.choice(['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
		
		def set_value(number):
			val = {'A': 11,
				   'J': 10,
				   'Q': 10,
				   'K': 10}
			if number in val:
				return val[number]
			else:
				return number

		self.value = set_value(self.number)


	def get_color(self):
		return self.color

	def get_number(self):
		return self.number

	def get_value(self):
		return self.value

	def get_card(self):
		return "This is a {} {}".format(self.color, self.number)

	def __str__(self):
		return "This is a {} {}".format(self.color, self.number)

def set_points(cards):
	points = 0
	for card in cards:
		points += card.get_value()
	return points

class Player(object):
	def __init__(self, name = None):
		self.points = 0
		self.cards = [Card() for x in xrange(2)]
		if name == None:
			self.name = 'Player'
		else :
			self.name = name

		self.points = set_points(self.cards)

	def __str__(self):
		return '{} have {} points and {} cards.'.format(self.name, self.points, len(self.cards))

	def get_points(self):
		return self.points

	def get_cards(self):
		for card in self.cards:
			if card is not None:
				print card.get_card()

	def get_new_card(self):
		if self.points < 21:
			self.cards.append(Card())
			self.points = set_points(self.cards)
		else:
			print 'Cannot get new cards'

class Dealer(Player):
	def __init__(self):
		self.points = 0
		self.cards = [Card() for x in xrange(2)]
		self.name = 'Dealer'
		self.points = set_points(self.cards)


###Testing Card 
# cardA = Card()
# print "The card is a {} {} and it's value is {}".format(cardA.get_color(), cardA.get_number(), cardA.get_value())
# print cardA

###Testig Player
# player = Player('Jesus')
# print player.get_cards()
# print player.get_points()
# print "Getting new card..."
# player.get_new_card()
# print player
# print player.get_points()

###Testing Dealer
dealer = Dealer()
print dealer
print "Getting new card..."
dealer.get_new_card()
print dealer

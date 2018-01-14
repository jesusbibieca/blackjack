#Blackjack

#Written by:	Jesus Bibieca
#Date:			Jan 14, 2018

import random as R

class Card(object):
	def __init__(self):
		self.color = None
		self.number =  R.choice(['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
		self.value = set_value(self.number)

	def set_value(self, number):
		val = {'A': 11,
			   'J': 10,
			   'Q': 10,
			   'K': 10}
		if number in val:
			return val[number]
		else:
			return number

	def get_color(self):
		return self.color

	def get_number(self):
		return self.number

	def get_value(self):
		return self.value

	def get_card(self):
		return "This is a {} {}".format(self.color, self.number)

	def __str__(self):
		return get_card(self)
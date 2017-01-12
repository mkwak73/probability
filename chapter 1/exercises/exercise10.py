#
# Chaper 1 - Exercise 10 - Martingale Doubling System
# Author: Michael Kwak
# Date: January 8 2017
#

#######################################################################################

#
# random () - return the next random floating point 
# number in the range [0.0, 1.0)
#

import random
from math import floor


#
# define roulette function which returns a value of [1,38]
#

def roulette():
	r = random.random()
	num = floor(38 * r) + 1
	return num


bet = 0
winnings = 0
wins = 0
losses = 0


while (-100 < winnings < 5):


	slot = roulette()

	# green or red; win

	if ((slot == 1) or (slot == 2) or (slot > 20)):

		winnings = winnings + bet
		wins = wins + 1
		bet = 1

		print("Slot:", slot, "\twon\twinnings: ", winnings, "\t\tnext bet: ", bet)

		
					

	# black; lose
	
	elif ((slot < 21) and (slot > 2)):
		
		winnings = winnings - bet
		losses = losses + 1
		bet = 2 * bet

		print("Slot:", slot, "\tlost\twinnings: ", winnings, "\t\tnext bet: ", bet)
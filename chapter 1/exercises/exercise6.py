# Chapter 1 - Exercise 6
# Author: Michael Kwak
# Date: December 31 2016
#######################################################

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


#
# total winnings, initialized to zero
# 

winnings = 0
print("Winnings: ", winnings)
print()


#
# each for-loop iteration is a game simulation of one spin of the roulette
#

for spin in range (1, 1000 + 1):

	#
	# one spin of roulette, return slot number
	# 

	slot = roulette()
	print("Slot: ", slot)


	#
	# define loss conditions
	# 1 and 2 represent 0 and 00 (green), lose $1
	# range [3,20] equals slots [1,18] on the roulette representing red, lose $1
	# range [21,38] equals slots [19,36] on the roulette representing black, win $1
	#

	if ((slot == 1) or (slot == 2) or (slot > 20)):

		winnings = winnings - 1
		print("Winnings: ", winnings)		

	elif ((slot < 21) and (slot > 2)):
		
		winnings = winnings +  1
		print("Winnings: ", winnings)

	print()






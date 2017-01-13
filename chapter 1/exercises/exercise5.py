# Chapter 1 - Exercise 5
# Author: Michael Kwak
# Date: December 30 2016

########################################################################################

#
# random () - return the next random floating point 
# number in the range [0.0, 1.0)
#

import random
from math import floor


#
# define dice function which simulates a roll of
# a single dice and returns a value of [1,6]
#

def dice():
	r = random.random()
	dice = floor(6 * r) + 1
	return dice


#
# j is an input that represents the number of times to simulate an n-roll game
#

j = int(input("Enter the number of games: "))


########################################################################################

#
# execute an n-roll game for j times
#

for n in range (1, 200 + 1):


	#
	# integer variable that counts the number of n-roll games 
	# that had at least one triple-sixes
	# 
	# needs to be initialized to zero for each new value of n
	#

	triple_sixes = 0


	for game in range (1, j + 1):

		#
		# boolean variable that turns true if a roll turns up all sixes
		#
		# needs to be initialized to zero before each game
		#	

		sixes = 0


		#
		# integer variable that keeps track of the i-th roll 
		# in a game all the way until n
		#
		# needs to be initialized to zero before each game
		#

		roll = 0

		
		#
		# simulate an n-roll game
		#

		while ((sixes != 1) and (roll < n)):

			#
			# a roll of 3 dice
			#

			dice1 = dice()
			dice2 = dice()
			dice3 = dice()


			#
			# determine if the roll turned up all sixes
			#

			if ((dice1 == 6) and (dice2 == 6) and (dice3 == 6)):
				sixes = 1
				triple_sixes = triple_sixes + 1
		

			#
			# increment roll
			#

			roll = roll + 1

	#
	# print the results
	#

	print("n =", n, "prob =", triple_sixes / j)






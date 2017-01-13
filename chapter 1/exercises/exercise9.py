# Chapter 1 - Exercise 9 - Labouchere system
# Author: Michael Kwak
# Date: January 4 2016

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


#
# define bet function which returns the sum
# of the first and last numbers of the list
#

def sum(list):
	
	if (len(list) == 1):

		sum = list[0]

	else:
		last = len(list) - 1
		sum = list[0] + list[last]
	
	return sum



#
# define delete function which removes
# the first and last numbers from the list
#

def delete(list):

	if (len(list) == 1):

		del list[0]

	else:
	
		last = len(list) - 1

		# delete last number (first!!)
		del list[last]

		# delete first number
		del list[0]

	return list



#
# check to see that list is not empty
# return 1 if not empty
# return 0 if empty
#

def not_empty(list):

	if (len(list) > 0):
		return 1

	elif (len(list) == 0):
		return 0 

#######################################################################################

#
# define variables to tally wins and losses
# initialize to zero
#

wins = 0
losses = 0


#
# define initial list
#

list = [1,2,3,4]
print("list: ", list)


#
# define variable to tally winnings in dollar amount
# initialize to zero
#

winnings = 0


#
# total number of turns that occurred in a single game
# initialize to zero
#

turns = 0


#######################################################################################
#######################################################################################


while not_empty(list):

	bet = sum(list)
	print("bet: ", bet)

	slot = roulette()
	print("slot: ", slot)


	# green or red; win

	if ((slot == 1) or (slot == 2) or (slot > 20)):

		winnings = winnings + bet
		list = delete(list)
		wins = wins + 1

		print("Won - modified list after delete: ", list)
		print("Winnings: ", winnings)	
		print()
		
					

	# black; lose
	
	elif ((slot < 21) and (slot > 2)):
		
		winnings = winnings - bet
		list.append(bet)
		losses = losses + 1

		print("Lost - modified list after append: ", list)
		print("Winnings: ", winnings)
		print()


	#increment turn per 1 interation of while loop
	
	turns = turns + 1

#######################################################################################

print("Total winnings for this game: ", winnings)
print()
print("Total number of turns: ", turns)
print("Total number of wins: ", wins)
print("Total number of losses: ", losses)
print("Win ratio: ", wins / turns)
print("Loss ratio ", losses / turns)












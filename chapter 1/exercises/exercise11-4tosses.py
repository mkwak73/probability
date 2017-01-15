#
# Chapter 1 - Exercise 11 - Modified HTSimulation - 4 tosses
# Author: Michael Kwak
# Date: January 14 2017
#


# FUNCTION DECLARATION, VARIABLE INITIALIZATIONS AND OTHER PREP WORK
#######################################################################################

#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random


#
# tosses represents the number of coin tosses in a single game
#

tosses = 4


#
# define heads or tails generating random function
#

def headtail():

	num = random.random()

	#
	# heads in range [0.0, 0.5)
	#

	if (num < 0.5):
		return "H"

	#
	# tails in range [0.5, 1.0)
	#

	else:
		return "T"
	

# 
# winnings is a list structure to track Peter's winnings per turn in a 4 roll game
# if i is the index value of each list element, the (i + 1)th element contains 
# the winnings value for the (i + 1)th turn
# example - [1, ...] means winnings equal to 1 for the 1st turn


winnings = [0, 0, 0, 0]


#
# winnings_dist is a dictionary structure where the key represents the
# total winnings and the value is the frequency of that particular key
#

winnings_dist = {0:0, 2:0, 4:0}


# PRELIMINARY STUFF
#######################################################################################


#
# plays represents the total number of times the game is played
#

plays = int(input("Enter the number of plays: "))


#
# Open output file for recording the proportion of times Peter's total winnings
# take on values 0, 2, 4
#

output_file = open('/home/pi/py3prog/probability/chapter 1/output/exercise11-4tosses-output.txt', 'w')


# CORE LOGIC
#######################################################################################


#
# simulate for the number of times equal to plays
#

for play in range (0, plays):

	#
	# everything below represents the mechanics for a single game
	#

	#
	# j is Peter's winnings, which varies per roll
	#

	j = 0


	print()
	print()

	#
	# calculate Peter's j through a 4 roll game
	#

	for roll in range (0, tosses):

		toss_result = headtail()

		#
		# condition for heads
		#

		if (toss_result == 'H'):

			print("H", end = "")
			j = j + 1

		#
		# condition for tails
		#

		elif (toss_result == 'T'):

			print("T", end = "")
			j = j - 1
	

		#
		# distribute Peter's j per roll/turn into winnings list
		#

		winnings[roll] = j


		#
		# after the 4 roll for-loop concludes, the final value
		# of j is Peter's total winnings for that game
		#

		total_winnings = j


	#
	# display the fully populated winnings list
	# 

	print()
	print("winnings:", winnings)


	#
	# determine the max value in the winnings list and display it
	#

	print("max winnings:", max(winnings))


	#
	# display total winnings
	#

	print("total winnings:", total_winnings)


	#
	# check that total_winnings is a positive, even number
	# increment the value (frequency) for that particular key (total_winnings)
	# display populated winnings_dist
	#

	if ((total_winnings % 2) == 0) and (total_winnings >= 0):
		winnings_dist[total_winnings] = winnings_dist[total_winnings] + 1

	print("winnings_dist:", winnings_dist)


# DATA GATHERING AND WRAP-UP
#######################################################################################


#
# re-purpose variable total_winnings; initialize to zero
#

total_winnings = 0


#
# now outside of any core logic loops
# winnings_dist is fully populated; loop through winnings_dist to
# properly format the data and write to corresponding output text files
#

while  (0 <= total_winnings <= 4):
	game_data =  str(total_winnings) + ' ' + str(winnings_dist[total_winnings]/plays) + '\n'
	output_file.write(game_data)
	
	total_winnings = total_winnings + 2


# close output file

output_file.close()

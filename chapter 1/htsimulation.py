#
# Chapter 1 - HTSimulation
# Author: Michael Kwak
# Date: November 25 2016
#


# VARIABLE INITIALIZATIONS AND OTHER PREP WORK
#######################################################################################

import random

#
# n represents the number of coin tosses in a single game
#

n = 40

# 
# dictionary structures to record Peter's winnings and lead distributions
# roll_dist tracks Peter's winnings for each turn in a 40 roll game
#

winnings_dist = {-20:0, -19:0, -18:0, -17:0, -16:0, -15:0, -14:0, -13:0, -12:0, -11:0, -10:0, -9:0, -8:0, -7:0, -6:0, -5:0, -4:0, -3:0, -2:0, -1:0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0 , 20:0}

lead_dist = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0 , 20:0, 21:0, 22:0, 23:0, 24:0, 25:0, 26:0, 27:0, 28:0, 29:0, 30:0, 31:0, 32:0, 33:0, 34:0, 35:0, 36:0, 37:0, 38:0, 39:0, 40:0}

roll_dist = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0 , 20:0, 21:0, 22:0, 23:0, 24:0, 25:0, 26:0, 27:0, 28:0, 29:0, 30:0, 31:0, 32:0, 33:0, 34:0, 35:0, 36:0, 37:0, 38:0, 39:0, 40:0}


# PRELIMINARY STUFF
#######################################################################################


#
# plays represents the total number of times the game is played
#

plays = int(input("Enter the number of plays: "))


#
# Open output files for recording winnings and lead distribution data
#

winningsdistributionoutput_file = open('/home/pi/py3prog/chapter 1/output/winningsdistribution.txt', 'w')
leaddistributionoutput_file = open('/home/pi/py3prog/chapter 1/output/leaddistribution.txt', 'w')


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
	# lead is the number of times Peter is in the lead
	#

	j = 0
	lead = 0


	print()
	print()
	print()

	#
	# calculate Peter's j through a 40 roll game
	#

	for roll in range (1,n + 1):

		#
		# condition for heads
		#

		if (random.random() < 0.5):
			print("H", end = "")
			j = j + 1

		#
		# condition for tails
		#

		else:
			print("T", end = "")
			j = j - 1
	

		#
		# distribute Peter's j per roll/turn into roll_dist
		#

		roll_dist[roll] = j


		#
		# after the 40 roll for-loop concludes, the final value
		# of j is Peter's total winnings for that game
		#

	
	print()
	print()
	print("roll_dist:", roll_dist)	
	print()
	print("Peter's total winnings:", j)


	#
	# distribute total winnings into winnings_dist
	# the final value of j is the key of the winnings_dist dictionary structure
	# increment the corresponding value for that particular key
	#
	# example: for the first game simulated, if the total winnings result is 7, 
	# then the key is 7, its value becomes 1 (formerly initialized to zero), 
	# and the dictionary element now becomes {..., 7:1, ...}
	#
	# do this only for final j values between -21 and 20 to comply with the 
	# boundary limits of winnings_dist
	#

	if (j < 21) and (j > -21):	
		winnings_dist[j] = winnings_dist[j] + 1


	#
	# loop through roll_dist and calculate the total number of times Peter was
	# in the lead (variable lead) for this game following the convention that 
	# when Peter's j is zero, he is in the lead if he was ahead at the previous 
	# toss and not if he was behind at the previous roll
	#
	# the final value of lead is the total number of times Peter was in the lead 
	#

	for roll in range (1,n + 1):
		if (roll_dist[roll] > 0):
			lead = lead + 1
		if (roll_dist[roll] == 0):
			if (roll_dist[roll - 1] > 0):
				lead = lead + 1
	

	print("Total number of times Peter was in the lead:", lead)


	#
	# distribute lead into lead_dist
	# the final value of lead is the key of the lead_dist dictionary structure
	# increment the corresponding value for that particular key
	#
	# example: for the first game simulated, if the final value of lead is 7, 
	# then the key is 7, its value becomes 1 (formerly initialized to zero), 
	# and the dictionary element now becomes {..., 7:1, ...}
	#
	# do this only for final lead values between 0 and 40 to comply with the 
	# boundary limits of lead_dist
	#

	if (0 <= lead) and (lead <= 40):
		lead_dist[lead] = lead_dist[lead] + 1


# DATA GATHERING AND WRAP-UP
#######################################################################################


#
# now outside of any core logic loops
# winnings_dist and lead_dist are fully populated
# properly format the data and write to corresponding output text files
#

for winnings in range (-20, 21):
	game_data = str(winnings) + ' ' + str(winnings_dist[winnings]/plays) + '\n'
	winningsdistributionoutput_file.write(game_data)

for leads in range (0, 41):
	game_data = str(leads) + ' ' + str(lead_dist[leads]/plays) + '\n'
	leaddistributionoutput_file.write(game_data)


#
# close output files
#

winningsdistributionoutput_file.close()
leaddistributionoutput_file.close()


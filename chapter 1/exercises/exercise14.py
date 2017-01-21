#
# Chapter 1 - Exercise 14 - Paid 2^j dollars on j-th toss
# Author: Michael Kwak
# Date: January 20 2017
#


# FUNCTION DECLARATION, VARIABLE INITIALIZATIONS AND OTHER PREP WORK
#######################################################################################

#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random


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
# define pay distribution dictionary
# the keys represent values of pay, in powers of 2, where pay = 2^j dollars for the j-th toss
# the values represent the proportion of times the corresponding key (pay) occurred for the entire simulation
#

pay_dist = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0, 512:0, 1024:0, 2048:0, 4096:0, 8192:0, 16384:0, 32768:0, 65536:0, 131072:0, 262144:0, 524288:0, 1048576:0, 2097152:0, 4194304:0}


#
# pay_to_play is the summation over the entire range of pay [2, 4, ..] of (pay) * (proportion of pay)
#

pay_to_play = 0


# PRELIMINARY STUFF
#######################################################################################


#
# plays represents the total number of times the game is played
#

plays = int(input("Enter the number of plays: "))

output_file = open('/home/pi/py3prog/probability/chapter 1/output/exercise14-output.txt', 'w')
 


# CORE LOGIC
#######################################################################################


#
# simulation loop
# 

for game in range(1, plays + 1):
	
	print()
	print("Game:", game)
	
	j = 1
	pay = 0
	coin = 'T'

	#
	# start of game execution loop
	# 

	while (coin != 'H'):
		
		coin = headtail()
		print(coin)
	
		if coin == 'H':
			pay = 2 ** j
		
		print("j =", j, "pay:", pay)
		
		j = j + 1
		
	#
	# end of game execution loop
	#
		
	game = game + 1
	
	pay_dist[pay] = pay_dist[pay] + 1
	
#
# end of simulation loop
# 


# DATA GATHERING AND WRAP-UP
#######################################################################################


pay_dist_keys = pay_dist.keys()


#
# convert the frequency of pay into proportion
# calculate the summation
#

for pay in pay_dist_keys:
	
	pay_dist[pay] = pay_dist[pay] / plays
	
	pay_to_play = pay_to_play + pay * pay_dist[pay]
	
	game_data = str(pay) + ' ' + str(pay_dist[pay]) + '\n'
	output_file.write(game_data)	


print()
print("Pay to play amount:", pay_to_play)




# close output file

output_file.close()

# Chapter 1 - Exercise 7 - second visit to Las Vegas
# Author: Michael Kwak
# Date: January 1 2017

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
# total winnings, initialized to zero
# 

winnings = 0


#
# instantiate an output file for data
#

ex7_sec_output_file = open('/home/pi/py3prog/output/ex7_sec_output.txt', 'w') 


#######################################################################################

#
# each for-loop iteration is a game simulation of one spin of the roulette
#

for spin in range (1, 500 + 1):

	#
	# one spin of roulette, return slot number
	# 

	slot = roulette()


	#
	# if ball stops on 17 (slot num = 19), win $1 back plus $35
	# otherwise, lose $1
	#

	ex7_sec_output_file.write(str(spin)) 
	ex7_sec_output_file.write(" ") 

	if (slot == 19):

		winnings = winnings + 1 + 35
		ex7_sec_output_file.write(str(winnings))
		ex7_sec_output_file.write("\n")		

	else:
		
		winnings = winnings - 1
		ex7_sec_output_file.write(str(winnings))
		ex7_sec_output_file.write("\n")


#######################################################################################

ex7_sec_output_file.close()







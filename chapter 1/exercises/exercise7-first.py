# Chapter 1 - Exercise 7 - first visit to Las Vegas
# Author: Michael Kwak
# Date: December 31 2016

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

ex7_first_output_file = open('/home/pi/py3prog/output/ex7_first_output.txt', 'w') 


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
	# define loss conditions
	# 1 and 2 represent 0 and 00 (green), lose $1
	# range [3,20] equals slots [1,18] on the roulette representing red, lose $1
	# range [21,38] equals slots [19,36] on the roulette representing black, win $1
	# write the results to the output file for plotting later with Mathematica
	#

	ex7_first_output_file.write(str(spin)) 
	ex7_first_output_file.write(" ") 

	if ((slot == 1) or (slot == 2) or (slot > 20)):

		winnings = winnings - 1
		ex7_first_output_file.write(str(winnings))
		ex7_first_output_file.write("\n")		

	elif ((slot < 21) and (slot > 2)):
		
		winnings = winnings +  1
		ex7_first_output_file.write(str(winnings))
		ex7_first_output_file.write("\n")


#######################################################################################

ex7_first_output_file.close()







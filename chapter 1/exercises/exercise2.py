# Chapter 1 - Exercise 2
# Author: Michael Kwak
# Date: December 27 2016
#######################################################

#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random


#
# get input for number of tosses for this simulation
#

n = int(input("Enter the value of n: "))


#
# initialize plays to zero
# initialize inside, outside to zero
#

plays = 0
inside = 0
outside = 0


while (plays < 100):

	#
	# initialize head, tail counters to zero
	#

	heads = 0
	tails = 0

	#
	# run simulation by generating heads or tails 
	# using random number generator
	#

	for tosses in range (1,n+1):
		if (random.random() < 0.5):
			heads = heads + 1
		else:
			tails = tails + 1

	#
	# determine whether or not the proportion of heads 
	# is within .1 of .5 (between .4 and .6) 
	# "inside" is a variable signifying "within the interval"
	# increment while loop control variable "plays"
	#
	
	proportion_of_heads = heads / tosses

	if ((proportion_of_heads > 0.4) and (proportion_of_heads < 0.6)):
		inside = inside + 1
	else:
		outside = outside + 1

	plays = plays + 1
	
#
# report results
#

print("Plays: ", plays)	
print("Inside: ", inside) 
print("Outside: ", outside)
print()

		 


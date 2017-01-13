# Chapter 1 - Exercise 1
# Author: Michael Kwak
# Date: December 26 2016
#######################################################

#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random


#
# get input for number of tosses for this simulation
#

n = int(input("Enter the value of n: "))
print()


#
# initialize head and tail counters to zero
# initialize number of tosses to zero
#

heads = 0
tails = 0
tosses = 0


#
# run simulation by generating heads or tails 
# using random number generator
#

for index in range (1,n+1):
	if (random.random() < 0.5):
		heads = heads + 1
		tosses = tosses + 1
	else:
		tails = tails + 1
		tosses = tosses + 1

#
# print every 100 times:
# a. the proportion of heads minus 1/2 
# b. the number of heads minus half the number of tosses
#
	
	if (tosses % 100 == 0):
		proportion_of_heads = heads / tosses
		approach_to_zero_1 = proportion_of_heads - 0.5
		approach_to_zero_2 = heads - int(tosses / 2)
				
		print("Number of tosses: ", tosses) 
		print("Proportion of heads minus 0.5: ", approach_to_zero_1) 
		print("Number of heads minus half the number of tosses: ", approach_to_zero_2)
		print()

		 


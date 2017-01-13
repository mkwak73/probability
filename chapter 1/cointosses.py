#
# Chapter 1 - Coin Tosses
# Author: Michael Kwak
# Date: November 21 2016
#

#######################################################################################

import random

n = int(input("Enter the value of n: "))

heads = 0
tails = 0

for index in range (0,n):
	if (random.random() < 0.5):
		print("H", end = "")
		heads = heads + 1
	else:
		print("T", end = "")
		tails = tails + 1
print()
print("Heads: ", heads) 
print("Tails: ", tails)
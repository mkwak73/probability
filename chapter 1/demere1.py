# DeMere1
# Author: Michael Kwak
# Date: November 22 2016
#######################################################

import random
import math

n = int(input("Enter the value of n: "))

wins = 0

for play in range (0,n):

	six = 0

	for roll in range (0,4):

		die_value = math.floor(6 * random.random()) + 1
 
		if (die_value == 6):
			six = six + 1
		
	print(six, end = "")

	if (six >= 1):
		wins = wins +1
		print(" win")
	else:
		print(" lose")

print("A six came up in the first four rolls", (wins / n) * 100  ,"percent of the time.") 
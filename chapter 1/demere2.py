# DeMere2
# Author: Michael Kwak
# Date: November 22 2016
#######################################################

import random
import math

plays = int(input("Enter the number of plays: "))
n = int(input("Enter the value of n: "))

wins = 0

for play in range (0,plays):

	pair_six = 0
	roll = 0

	while (roll < n) and (pair_six == 0) :
		
		roll1 = math.floor(6 * random.random()) + 1
		roll2 = math.floor(6 * random.random()) + 1
 
		if (roll1 == 6) and (roll2 == 6):
			pair_six = 1
		
		roll = roll + 1

	if (pair_six == 1):

		wins = wins +1
		print("win")

	else:

		print("lose")

print("For", plays,"plays and", n,"rolls for each play, " +\
"a pair of sixes occurred", (wins / plays) * 100 , "percent of the time.") 
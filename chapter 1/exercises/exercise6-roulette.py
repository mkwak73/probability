# Chapter 1 - Exercise 6 - 38 slot roulette wheel demo
# Author: Michael Kwak
# Date: December 31 2016
#######################################################

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
# j is an input that represents the number of times 
# to simulate a single turn roulette game
#

j = int(input("Enter the number of games: "))


#
# the index of each list element represents the slot number
# the value is the amount of times that slot number materialized for j games
#

slot = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


for turn in range (1, j + 1):

	slot_num = roulette()
	slot[slot_num] = slot[slot_num] + 1
	
print()

for i in range (1, 38 + 1):

	print(i, slot[i])	


# 1 / 38 = 0.026315789
# results:
#
# Enter the number of games: 10000000

# 1 263286
# 2 263362
# 3 262931
# 4 264038
# 5 262859
# 6 263267
# 7 263627
# 8 263454
# 9 262907
# 10 262479
# 11 263905
# 12 262801
# 13 263170
# 14 263143
# 15 263001
# 16 262906
# 17 262376
# 18 263440
# 19 262095
# 20 262447
# 21 263934
# 22 262886
# 23 263359
# 24 263188
# 25 263091
# 26 262508
# 27 263906
# 28 262775
# 29 262985
# 30 263400
# 31 263166
# 32 263581
# 33 263076
# 34 263498
# 35 262473
# 36 263413
# 37 263256
# 38 264011







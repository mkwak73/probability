# Dice Roll
# Author: Michael Kwak
# Date: January 4 2017
#######################################################

import random
import math

n = 1000000

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for i in range (1,n):
	
	diceroll = math.floor(6 * random.random()) + 1 

	if (diceroll == 1):
		
		one = one + 1

	elif (diceroll == 2):
		
		two = two + 1

	elif (diceroll == 3):

		three = three + 1

	elif (diceroll == 4):

		four = four + 1

	elif (diceroll == 5):

		five = five + 1

	elif (diceroll == 6):

		six = six + 1

print("Prob of 1: ", one / n);
print("Prob of 2: ", two / n);
print("Prob of 3: ", three / n);
print("Prob of 4: ", four / n);
print("Prob of 5: ", five / n);
print("Prob of 6: ", six / n);
#
# Chaper 1 - Random Numbers
# Author: Michael Kwak
# Date: January 6 2017
#

#######################################################################################

import random

#
# input n - number of random numbers to generate
#

n = int(input("Enter the value of n: "))
print()


#
# initialize loop control variable
#

i = 0

#
# generate n random numbers to 6 decimal places in tabbed rows of 4 columns
#

while (i < n):

	j = 0
	
	while ((j < 4) and (i < n)):
	
		num = random.random()
		print("{0:.6f}\t".format(num), end="")
		j= j + 1
		i= i + 1

	print()
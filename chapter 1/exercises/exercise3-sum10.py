# Chapter 1 - Exercise 3 - Sum 10 Triple Integers Table Generation
# Author: Michael Kwak
# Date: December 28 2016
#######################################################

#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random
from math import floor

def dice():
	r = random.random()
	dice = floor(6 * r) + 1
	return dice

exercise3_sum10_output_file = open('/home/pi/py3prog/chapter 1/exercise3_sum10_output.txt', 'w')

for j in range (0,1000000):	
	dice1 = dice()
	dice2 = dice()
	dice3 = dice()

	sum = dice1 + dice2 + dice3

	if (sum == 10):

		exercise3_sum10_output_file.write(str(dice1))
		exercise3_sum10_output_file.write(str(dice2))
		exercise3_sum10_output_file.write(str(dice3))
		exercise3_sum10_output_file.write("\n")

exercise3_sum10_output_file.close()

#
# execute the following commands afterwards:
#   cat exercise3_sum10_output.txt | sort | uniq
#   cat exercise3_sum10_output.txt | sort | uniq | wc -l
#

# results:
# 136
# 145
# 154
# 163
# 226
# 235
# 244
# 253
# 262
# 316
# 325
# 334
# 343
# 352
# 361
# 415
# 424
# 433
# 442
# 451
# 514
# 523
# 532
# 541
# 613
# 622
# 631
#
# 27






		 


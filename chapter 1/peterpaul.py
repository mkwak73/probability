# Peter and Paul
# Author: Michael Kwak
# Date: November 24 2016
#######################################################

import random

# n represents the number of coin tosses in a single play
n = 40

# j represents Peter's winnings
j = 0

peterpauloutput_file = open('/home/pi/py3prog/output/peterpauloutput.txt', 'w')

peterpauloutput_file.write("0 0\n")

for roll in range (1,n + 1):
	if (random.random() < 0.5):
		print("H", end = "")
		j = j + 1
		roll_data = str(roll) + ' ' + str(j) + '\n'
		peterpauloutput_file.write(roll_data)
		
	else:
		print("T", end = "")
		j = j - 1
		roll_data = str(roll) + ' ' + str(j) + '\n'
		peterpauloutput_file.write(roll_data)

print()
peterpauloutput_file.close()


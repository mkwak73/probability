#
# Chapter 1 - Exercise 16 - boys and girls - part 2 (at least 1 boy and 1 girl)
# Author: Michael Kwak
# Date: January 24 2017
#


# FUNCTION DECLARATIONS
#######################################################################################

#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random


#
# define boy or girl generating random function
#

def boygirl():

	num = random.random()

	#
	# baby boy probability range [0.0, 0.49)
	#

	if (0 <= num < 0.5):
		return "B"

	#
	# baby girl probability range [0.49, 1.0)
	#

	elif (0.5 <= num < 1.0):
		return "G"
	

# PRELIMINARY STUFF
#######################################################################################

num_fam = int(input("Enter number of families to simulate: "))


# CORE LOGIC
#######################################################################################

#
# declare list to store the number of children for each family
#

family = []


#
# run simulation for number of families equal to 'num_fam'
#

for fam in range(1, num_fam + 1):
	
	boy = "F"
	girl = "F"
	num_child = 0
	
	
	#
	# generate random B/G string for each family
	# tally the number of children per family in variable 'num_child' 
	# add value of 'num_child' to list 'family'
	#
	
	print("Family", fam, ": ", end = "")
	
	while (boy != "T") or (girl != "T"):
	
		child = boygirl()
		print(child, end=" ")
		
		if child == "B":
			boy = "T"
		
		if child == "G":
			girl = "T"
			
		num_child = num_child + 1
		
	family.append(num_child)
	print()


#
# compute the total number of children contained in the list
# this will be used to later calculate the average number of children per family
#


total = 0

for fam in range(0,num_fam):
	total = total + family[fam]
	

# DATA REPORTING AND WRAP-UP
#######################################################################################


print()
print("Total number of children for all families:", total)
print("Average number of children per family:", total / num_fam)


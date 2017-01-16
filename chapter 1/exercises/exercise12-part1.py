#
# Chapter 1 - Exercise 12 - Poll - Part 1 (48% Republican / 52% Democratic / 1000 voters)
# Author: Michael Kwak
# Date: January 15 2017
#


# FUNCTION DECLARATION, VARIABLE INITIALIZATIONS AND OTHER PREP WORK
#######################################################################################

#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random


#
# define republican or democratic generating random function
#

def repdem():

	num = random.random()

	#
	# republican probability range [0.0, 0.48)
	#

	if (0 <= num < 0.48):
		return "R"

	#
	# democratic probability range [0.48, 1.0)
	#

	elif (0.48 <= num < 1.0):
		return "D"
	

#
# voters represents the number of voters in the poll
#

voters = 1000


#
# rep2 / dem2 represents the number of polls that resulted in Rep / Dem
# initialize to zero
#

rep2 = 0
dem2 = 0


# PRELIMINARY STUFF
#######################################################################################


n = int(input("Enter the number of polls to run: "))
print()


# CORE LOGIC
#######################################################################################


#
# run poll simulation n times, k-loop
#

for k in range (1, n + 1):
	
	#
	# rep1/dem1 represents the number of voters who voted Rep/Dem in a poll
	# initialize to zero inside of k loop, outside of i, j loop
	#

	rep1 = 0
	dem1 = 0
	
	#
	# dual loop control variables for formatting the printout of R / D outcomes
	# initialize to zero inside of k loop, outside of i, j loop
	# 

	i = 0
	j = 0
	
	#
	# logic for one poll simulation, i & j-loop
	#	

	while (i < voters):

		#
		# print a single 50 char length row of per voter R / D outcomes
		#
	
		for j in range (50):
		
			vote = repdem()
		
			print(vote, end="")
		
			#
			# count the number of voter outcomes for R and D
			#
			
			if (vote == "R"):
				rep1 = rep1 + 1
		
			elif (vote == "D"):
				dem1 = dem1 + 1
		
		print()
	
		i = i + 50
		
	print("Rep votes:", rep1)
	print("Dem votes:", dem1)
	
	#
	# outside of logic for one poll simulation, i & j-loop
	#
	
	#
	# count the number of polls resulting democratic
	#	
	
	if (dem1 > rep1):
		dem2 = dem2 + 1
		print("Poll", k, ": Democratic win")
		print()
	
	#
	# count the number of polls resulting republican
	#

	if (rep1 > dem1):
		rep2 = rep2 + 1
		print("Poll", k, ": Republican win")
		print()

#
# finished running poll simulation n times, outside of k-loop
#


# DATA GATHERING AND WRAP-UP
#######################################################################################


#
# of the polls simulated n times, printout number of R / D wins
#
	
print()
print("Rep win:", rep2)
print("Dem win:", dem2)

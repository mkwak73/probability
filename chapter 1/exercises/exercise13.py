#
# Chapter 1 - Exercise 13 - baby boys
# Author: Michael Kwak
# Date: January 18 2017
#


# FUNCTION DECLARATION, VARIABLE INITIALIZATIONS AND OTHER PREP WORK
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
	

#
# large/small represents the number of babies borm each day at large/small hospital
#

large = 45
small = 15


#
# large_60/small_60 are used to track the number of days where the percentage of 
# boys born exceed 60% at large/small hospital
# initialize to zero
#

large_60 = 0
small_60 = 0


#
# outer loop control variable for tracking day through the entire year
# 

day = 1


# CORE LOGIC
#######################################################################################

	
#
# START OF YEAR-LONG LOOP LOGIC
#	

while (day <= 365):

	#
	# START OF SINGLE DAY LOOP LOGIC
	# 
	
	#
	# large_boy is used to track the number of boys 
	# given birth on a given day at large hospital
	# initialize to zero
	#
			
	large_boy = 0
	
	#
	# small_boy is used to track the number of boys 
	# given birth on a given day at small hospital
	# initialize to zero
	#
			
	small_boy = 0


	print()
	print()
	print("Day", day)
	
	#
	# START OF SINGLE DAY LOOP - LARGE HOSPITAL - perform 45 births
	#
	
	print("Large hospital:")
		
	for birth in range (large):
		
		baby = boygirl()
		
		print(baby, end="")
		
		#
		# count the number of baby boys born in large hospital in a given day
		# boy_large is the main output of this large hospital loop
		#
			
		if (baby == "B"):
			large_boy = large_boy + 1
	
	#
	# END OF SINGLE DAY LOOP - LARGE HOSPITAL - perform 45 births
	#
	
	print()
	print("Number of baby boys born:", large_boy)
	print("Proportion of baby boys:", large_boy / large)  
			
	#
	# count the number of times baby boys born in
	# large hospital in a given day exceeds 60%
	#
	
	if ((large_boy / large) > 0.6 ):
		
		large_60 = large_60 + 1

		
	#
	# START OF SINGLE DAY LOOP - SMALL HOSPITAL - perform 15 births
	#
	
	print()
	print("Small hospital:")
		
	for birth in range (small):
			
		baby = boygirl()
		
		print(baby, end="")
		
	#
	# count the number of baby boys born in small hospital in a given day
	#
			
		if (baby == "B"):
			small_boy = small_boy + 1
	
	#
	# END OF SINGLE DAY LOOP - SMALL HOSPITAL - perform 15 births
	#
	
	print()
	print("Number of baby boys born:", small_boy)
	print("Proportion of baby boys:", small_boy / small)
	
	#
	# count the number of times baby boys born in
	# large hospital in a given day exceeds 60%
	#
	
	if ((small_boy / small) > 0.6 ):
		
		small_60 = small_60 + 1
	
	#
	# END OF SINGLE DAY LOOP LOGIC
	# 	
				
	
	#
	# increment year-long loop control variable
	#
	
	day = day + 1

#
# END OF YEAR-LONG LOOP LOGIC
#			



# DATA GATHERING AND WRAP-UP
#######################################################################################


#
# of the polls simulated n times, printout number of R / D wins
#
	
print()
print()
print()
print("The number of days where more than 60% of babies born were boys:")
print("Large hospital:", large_60)
print("Small hospital:", small_60)

# Chapter 1 - Horse Race
# Author: Michael Kwak
# Date: December 29 2016
#######################################################

#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random

#
# n represents the number of races
#

n = int(input("Enter the value of n: "))


#
# each following variable represents the amount of wins for each horse
#

acorn = 0
balky = 0
chestnut = 0
dolby = 0


#
# simulate the horse race
#

for race in range (1, n + 1):

	x = random.random()	
	
	if (x < 0.3):
		acorn = acorn + 1
		
	elif (0.3 <= x < 0.7):
		balky = balky + 1
	
	elif (0.7 <= x < 0.9):
		chestnut = chestnut + 1

	else:
		dolby = dolby + 1


#
# print the results
#


print()
print("Acorn wins: ", acorn)
print("Acorn won", (acorn / race) * 100, "percent of the time.")
print()
print("Balky wins: ", balky)
print("Balky won", (balky / race) * 100, "percent of the time.")
print()
print("Chestnut wins: ", chestnut)
print("Chestnut won", (chestnut / race) * 100, "percent of the time.")
print()
print("Dolby wins: ", dolby)
print("Dolby won", (dolby / race) * 100, "percent of the time.")



#
# Chapter 1 - Exercise 15 - Philadelphia 76ers Basketball Players
# Author: Michael Kwak
# Date: January 21 2017
#


# FUNCTION DECLARATION, VARIABLE INITIALIZATIONS AND OTHER PREP WORK
#######################################################################################


#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random


#
# define hit or miss generating random function
#

def hitmiss():

	num = random.random()

	#
	# hits in range [0.0, 0.5)
	#

	if (num < 0.5):
		return "H"

	#
	# misses in range [0.5, 1.0)
	#

	else:
		return "M"
		

#
# define a function that detects a streak of 5 or more hits in a 20 shot game
# a list 'x' is passed as a parameter
# the list contains 20 elements recording the hits or misses in a game
#

def streak(x):
	
	#
	# 'i' is a loop control variable to walk through the list
	#
	
	i = 0
	
	
	#
	# streak length of 5
	#
	
	streak_len = 5
	
	
	#
	# default return false
	#
	
	result = 'F'
	
	
	#
	# list length = 20 (20 shots in game)
	#
		
	list_len = len(x)
	
	
	#
	# main detection algorithm for streaks of 5 or more hits
	# stop executing the while-loop after a true is detected
	#
	
	while (i < (list_len - (streak_len - 1))) and result == 'F':
		
		if  (x[i] == 'H') and (x[i + 1] == 'H') and (x[i + 2] == 'H') and (x[i + 3] == 'H') and (x[i + 4] == 'H'):
			
			result = 'T'
			
		i = i + 1
		
	return(result)
	

#
# number of games where there was a streak
# initialized to zero
#

num_streaks = 0

	
# PRELIMINARY STUFF
#######################################################################################


games = int(input("Enter the number of games played:"))


# CORE LOGIC
#######################################################################################


#
# run simulation for 'games' number of times
#

for game in range(1, games + 1):	

	#
	# 'game_shots' is a list that records the hits (H) and misses (M) of a 20 shot game
	#
	
	game_shots = []

	#
	# produce a list of 20 random hits or misses
	#
	
	for shot in range(0,20):

		game_shots.append(hitmiss())

	#
	# print the list of 20 random hits or misses
	#
	
	print("Game", game, ":")

	for shot in game_shots:

		print(shot, end= " ")

	print()

	#
	# determine if the list contains a streak of 5 or more hits
	# count the number of games with a streak
	#
	
	s = streak(game_shots)
	
	if s == 'T':
		
		s = 'Yes'
		
		num_streaks = num_streaks + 1
		
	else:
		
		s = 'No'


# DATA REPORTING
#######################################################################################


	print("Was there a streak?", s)
	print("Proportion of games with streak:", num_streaks / games)
	print()
	



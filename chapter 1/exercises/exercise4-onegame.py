# Chapter 1 - Exercise 4 - one game only
# Author: Michael Kwak
# Date: December 29 2016
#######################################################

#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random


#
# each following variable represents whether I or the opponent is serving
#

my_serve = 1
opponent_serve = 0


#
# each following variable represents my and the opponent's score
#

my_score = 0
opponent_score = 0


#
# each following variable represents my and the opponent's number of wins
#

my_wins = 0
opponent_wins = 0


#
# run the game simulation
#

while ((my_score < 21) and (opponent_score < 21)):

	x = random.random()
	print(x)	
	
	if (my_serve == 1):
		if (x < 0.6):
			my_score = my_score + 1
			print("I win.")
			print("My score: ", my_score)
			print("Opponent score: ", opponent_score)
			print()
			print()
		else:
			my_serve = 0
			opponent_serve = 1
			print("Opponent serves next.")	
			print("My Serve: ", my_serve, "Opponent serve: ", opponent_serve)
			print()
			print()

	elif (opponent_serve == 1):
		if (x < 0.5):
			opponent_score = opponent_score + 1
			print("Opponent wins.")
			print("My score: ", my_score)
			print("Opponent score: ", opponent_score)
			print()
			print()
		else:
			my_serve = 1
			opponent_serve = 0
			print("I serve next.")
			print("My Serve: ", my_serve, "Opponent serve: ", opponent_serve)
			print()
			print()


if (my_score == 21):
	my_wins = my_wins + 1

if (opponent_score == 21):
	opponent_wins = opponent_wins + 1



#
# print the results
#


print()
print("My wins: ", my_wins, "Opponent wins: ", opponent_wins)



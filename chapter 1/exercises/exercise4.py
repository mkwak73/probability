# Chapter 1 - Exercise 4
# Author: Michael Kwak
# Date: December 29 2016
#######################################################

#
# random () - return the next random floating point number in the range [0.0, 1.0)
#

import random

#
# each following variable represents my and the opponent's number of wins
#

my_wins = 0
opponent_wins = 0

#
# n is an input that represents number of times to play the game
#

n = int(input("Enter the number of times to play the game :"))


#
# run the game simulation for n times
#

for game in range (1, n + 1):

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

	while ((my_score < 21) and (opponent_score < 21)):

		x = random.random()	
	
		if (my_serve == 1):
			if (x < 0.6):
				my_score = my_score + 1

			else:
				my_serve = 0
				opponent_serve = 1

		elif (opponent_serve == 1):
			if (x < 0.5):
				opponent_score = opponent_score + 1

			else:
				my_serve = 1
				opponent_serve = 0


	if (my_score == 21):
		my_wins = my_wins + 1

	if (opponent_score == 21):
		opponent_wins = opponent_wins + 1



#
# print the results
#


print()
print("My wins: ", my_wins, "Opponent wins: ", opponent_wins)
print("For", n, "games, the probability that I will win a game is", my_wins / n) 
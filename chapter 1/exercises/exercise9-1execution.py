# Chapter 1 - Exercise 9 - one execution of Labouchere system
# Author: Michael Kwak
# Date: January 4 2016
#######################################################

#
# random () - return the next random floating point 
# number in the range [0.0, 1.0)
#

import random
from math import floor


#
# define roulette function which returns a value of [1,38]
#

def roulette():
	r = random.random()
	num = floor(38 * r) + 1
	return num


#
# define bet function which returns the sum
# of the first and last numbers of the list
#

def sum(list):
	last = len(list) - 1
	sum = list[0] + list[last]
	return sum



#
# define delete function which removes
# the first and last numbers from the list
#

def delete(list):

	last = len(list) - 1

	# delete last number (first!!)
	del list[last]

	# delete first number
	del list[0]

	return list



#
# check to see that list is not empty
# return 1 if not empty
# return 0 if empty
#

def not_empty(list):

	if (len(list) > 0):
		return 1

	elif (len(list) == 0):
		return 0 


#
# initialize boolean variables for win or lose
#

win = 0
lose = 0


#
# define initial list
#

list = [1,2,3,4]



slot = roulette()
print("slot: ", slot)

print("list: ", list)

bet = sum(list)
print("bet: ", bet)

new_list = delete(list)
print("new list after delete: ", new_list)

list.append(19)
print("new list after add: ", list)

if not_empty(list):
	print("list: ", list, "list is not empty.")
else: 
	print("list: ", list, "list is empty.")

list=[]

if not_empty(list):
	print("list: ", list, "list is not empty.")
else: 
	print("list: ", list, "list is empty.")










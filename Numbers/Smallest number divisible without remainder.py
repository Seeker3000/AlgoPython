# Copyright (c) 2021 D.Damian
# Released under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
# ************************************************************************************************
# The following problem was inspired by Problem 5 (Smallest multiple) at Project Euler (projecteuler.net)
# ************************************************************************************************
# What is the smallest positive number that is divisible without any remainder by all of the numbers from X to Y?
# ************************************************************************************************
var_1 = input("Minimum value for the range: ")            # for example 1
var_2 = input("Maximum value for the range: ")            # for example 15

def function(item):
	for val in range(int(var_1),int(var_2)):
		if item % val != 0:
			return False
	return True


var_x = int(var_2)

while True:
    if function(int(var_x)):
        break
    else:
        var_x = int(var_x) + 1
            
print(var_x, 'is the smallest positive number that can be divided by each of the numbers from', var_1, 'to', var_2, 'without any remainder.')

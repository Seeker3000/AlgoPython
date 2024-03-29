# Copyright (c) 2021 D.Damian
# Released under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
# ************************************************************************************************
# The following problem is taken from Project Euler (projecteuler.net) where it has an ID 1 (Multiples of 3 and 5).
# ************************************************************************************************# ************************************************************************************************
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000. 
# ************************************************************************************************
val = 1000 # maximum value

def functie(val):
    container = []
    for i in range(1,val):
        if (i %5 ==0) or (i%3==0):
            container.append(i)
    return sum(container)

print('The sum of all the multiples of 3 or 5 below 1000 is: ', functie(val))

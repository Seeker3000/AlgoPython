# Copyright (c) 2020 D.Damian
# Released under the MIT license
# ************************************************************************************************
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

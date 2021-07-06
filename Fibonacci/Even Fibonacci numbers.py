# Copyright (c) 2021 D.Damian
# Released under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
# ************************************************************************************************
# The following problem is taken from Project Euler (projecteuler.net) where it has an ID 2 (Even Fibonacci numbers).
# ************************************************************************************************
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# ************************************************************************************************
Max_Fibonacci_number = 4000000
Sum = 0
next_val = 1
previous_val = 1

while(next_val < Max_Fibonacci_number):
    if next_val % 2 == 0:
          Sum += next_val
    storeprev = next_val
    next_val = next_val + previous_val
    previous_val = storeprev

print("The sum of the even-valued terms in the selected Fibonacci sequence is: " + str(Sum))

# Copyright (c) 2021 D.Damian
# Released under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
# ************************************************************************************************
# The following problem was inspired by Problem 6 (Sum square difference) at Project Euler (projecteuler.net)
# ************************************************************************************************
# What is the difference between the sum of the squares of the first X natural numbers and the square of the sum?
# ************************************************************************************************
import math

X = input("Number of positive natural numbers: ")            # for example 100
power = input("Enter the value for raised power: ")          # for example 2

maximum_number = int(X)+1

numbers_list = []

for i in range(1,maximum_number):
    numbers_list.append(i)

numbers_pow=list(map(lambda x:pow(x,int(power)),numbers_list))
numbers_pow_sum=sum(numbers_pow)

pow_numbers_sum=pow(sum(numbers_list),int(power))

print(pow_numbers_sum-numbers_pow_sum)

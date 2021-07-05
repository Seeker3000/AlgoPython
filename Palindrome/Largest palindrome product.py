# Copyright (c) 2020 D.Damian
# Released under the MIT license
# ************************************************************************************************
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# ************************************************************************************************
var_1 = input("What is the smallest n-digit number: ")        # 100 is the smallest 3 digit number
var_2 = input("What is the highest n-digit number: ")       # 999 is the highest 3 digit number

numbers_list=[]
palindromes_list=[]
numbers_range = range(int(var_1),int(var_2))

for item_1 in numbers_range:
    for item_2 in numbers_range:
        numbers_list.append(item_1*item_2)

def checker(message1):
       if str(message1) == str(message1)[: : -1]:     # using slices to find the palindrome
              palindromes_list.append(message1)


for item in numbers_list:
    checker(item)


print('The largest palindrome made from the product of two numbers in the range', var_1, 'to', var_2, 'is: ', max(palindromes_list))

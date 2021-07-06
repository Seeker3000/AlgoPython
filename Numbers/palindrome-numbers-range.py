# Copyright (c) 2021 D.Damian
# Released under the MIT license
# ************************************************************************************************
# check if range of numbers contains any palindrome (number which look the same when read forward and backward)
# Example numbers: 59395
# ************************************************************************************************
var_1 = input("What is the minimum number of the range:")
var_2 = input("What is the maximum number of the range:")

m = 1
for i in range(int(var_1), int(var_2)):
    product = i * m
    n = product
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print(product, "The number is a palindrome!")

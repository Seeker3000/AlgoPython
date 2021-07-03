# Copyright (c) 2020 D.Damian
# Released under the MIT license
# ************************************************************************************************
# check if word is palindrome: word which look the same when read forward and backward.
# Example words: Level
# Example numbers: 59395
# Example phrases: Top spot
# ************************************************************************************************
var = input("What is the mesage you wish to verify:")
message = var.replace(' ', '')                              # replaces all the empty spaces
message1 = message.casefold()

def checker(message1):
       if message1.upper() == message1[: : -1].upper():     # using slices to find the palindrome
              print(f"{var} is a palindrome")
       else:
              print('Not a palindrome')

checker(message1)

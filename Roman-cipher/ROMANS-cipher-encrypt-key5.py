# Copyright (c) 2020 D.Damian
# Released under the MIT license
# ************************************************************************************************
# All letters of the message are converted to upper case as the Romans used only capital letters
# The cipher alphabet is the plain alphabet shifted left or right by some number of positions
# Example Plain:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Example Cipher:   XYZABCDEFGHIJKLMNOPQRSTUVW  -- uses 23 shift right positions
# ************************************************************************************************
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
var = input("What is the mesage you wish to encrypt:")
message = ''                                                # empty string to hold the encrypted message
for letter in var:
       letter = letter.upper()                              # if letter is not the upper case, then convert it to upper case
       letterIDX = alphabet.find(letter)
       if letterIDX == -1:
           message += letter
       else:
           letterIDX += 5
           if letterIDX >= len(alphabet):
                letterIDX -= len(alphabet)
           elif letterIDX < 0:
                letterIDX += len(alphabet)
           message += alphabet[letterIDX]
print('Your encrypted text in key 5 is:', message)

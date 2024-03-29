# Copyright (c) 2021 D.Damian
# Released under the MIT license
# ************************************************************************************************
# check if word pairs are anagrams: words formed by rearranging the letters of a different word or phrase, while using all the original letters exactly once
# Example numbers: 59395
# Example phrases: a gentleman -- elegant man
# ************************************************************************************************
var1 = input("First word:")
var2 = input("Second word:")

word1 = var1.casefold()
word2 = var2.casefold()

def checker(word1, word2):
    if(sorted(word1) == sorted(word2)):
        print(f"{var1} and {var2} are anagrams")  
    else: 
        print("Not anagrams")

checker(word1, word2) 

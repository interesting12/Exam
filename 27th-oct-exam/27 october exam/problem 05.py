
# 5) Palindrome Checker (3 ქულა)
# Create a program that checks if a given string is
#  a palindrome (reads the same forward and backward). 
# The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False

import string
def palindrome(ttt):
    str = ''.join(char.lower() for char in ttt if char.isalnum())
    return str == str[::-1]

print(palindrome ("A man a plan a canal Panama"))


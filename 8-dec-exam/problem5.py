
# Problem 5: Check if Two Strings are Anagrams - 5ქ
# Challenge:
#  Write a function to check if two strings are anagrams (contain the same characters in the same frequency).
# Instructions:
# Input: Two strings (e.g., "listen" and "silent").
# Output: A boolean (True or False) indicating if the strings are anagrams.
# Test Cases:
# assert are_anagrams("listen", "silent") == True
# assert are_anagrams("hello", "world") == False
# assert are_anagrams("triangle", "integral") == True

def anagrams( str1, str2): # შევქმნათ ფუნქცია ორი პარამეტრით
    if len(str1) != len(str2): #შევამოწმოთ, თუ პირველი პარამეტრის სიგრძე (len) არ უდრის მეორე პარამეტრის სიგრძეს : 
        return False #დააბრუნოს ბულეან მნიშვნელობა False
    elif len(str1) == len(str2): #შევამოწმოთ, თუ პირველი პარამეტრის სიგრძე (len) უდრის მეორე პარამეტრის სიგრძეს : 
        return True #დააბრუნოს ბულეან მნიშვნელობა True
    
print(anagrams("listen", "silent"))


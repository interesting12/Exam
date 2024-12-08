# Problem 1: Sum of Positive Numbers - 2ქ
# Challenge:
#  Create a function that takes a list of numbers and returns the sum of all positive numbers.
# Instructions:
# Input: A list of integers (e.g., [1, -4, 7, 12]).
# Output: The sum of all positive integers in the list.
# Test Cases:
# assert problem_1_sum_of_positive([1, -4, 7, 12]) == 20
# assert problem_1_sum_of_positive([-1, -2, -3, -4]) == 0
# assert problem_1_sum_of_positive([]) == 0

def sum_of_positive_numbers( nums): #შევქმნათ ფუნქცია
    num = 0 #დავადეკლალიროთ ცვლადი num და გავუტოლოთ 0-ს
    for i in nums: # გადავუაროთ foor loop- ით ფუნქციის პარამეტრს
        if i > 0: # შევამოწმოთ, თუ საიტერაციო ცვლადი მეტია 0-ზე num ცვლადი გავზარდოთ iთ
            num += i
    return num # დავაბრუნოთ num ცვლადის საბოლოო ვერსია 

         
print(sum_of_positive_numbers([-1, -2, -3, -4])) 

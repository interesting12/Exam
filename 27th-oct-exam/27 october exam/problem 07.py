# # 7) Fibonacci Sequence Generator (4 ქულა)
# Create a program that receives an integer n and returns the
#  first n numbers in the Fibonacci sequence. The sequence 
# starts with 0 and 1, and each subsequent number is the sum
#  of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]


def fibonacci_sequence(num): 
    if num <= 0:
        return[]
    elif num == 1: 
        return[0]
    
    sequence = [0, 1 ]
    for i in range(2, num):
        fibonacci_sum = sequence[-1] + sequence[-2]
        sequence.append(fibonacci_sum)

    return sequence[:num]
        
print(fibonacci_sequence(6))

        
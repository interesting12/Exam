def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisor = 3
result = divisible_by(numbers, divisor)
print(result)  
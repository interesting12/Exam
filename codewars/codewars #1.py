def min_sum_of_products(nums):
    nums.sort()
    n = len(nums)
    min_sum = 0
    for i in range(0, n, 2):
        if i + 1 < n:
            min_sum += nums[i] * nums[i + 1]
    return min_sum


nums = [3, 1, 4, 2]
result = min_sum_of_products(nums)
print(result) 
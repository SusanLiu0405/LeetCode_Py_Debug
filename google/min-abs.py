def min_abs(nums):
    total = sum(nums)
    result = abs(total)
    for num in nums:
        curr_result = abs(total - 2 * num)
        result = min(curr_result, result)
    return result
nums = [4, -3, 5, -7]
print(min_abs(nums))
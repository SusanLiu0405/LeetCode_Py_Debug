def sort_and_join(nums):
    n = len(nums)
    min_val = [0] * n
    min_val[-1] = nums[-1]
    result = 0
    left_max = float('-inf')
    for i in range(n - 2, -1, -1):
        min_val[i] = min(nums[i], min_val[i + 1])
        
    for i in range(len(nums) - 1):
        left_max = max(nums[i], left_max)
        right_min = min_val[i + 1]
        if left_max <= right_min:
            result += 1
    return result
nums = [1, 2, 3, 4]
print(sort_and_join(nums))
'''
right to left, find min:

'''
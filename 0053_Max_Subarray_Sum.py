# 求当前数组里的子数组，要求：得到最大的总和，并返回。
from typing import *
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for curr in nums[1:]:
            curr_sum = max(curr_sum + curr, curr)
            max_sum = max(max_sum, curr_sum)
        return max_sum
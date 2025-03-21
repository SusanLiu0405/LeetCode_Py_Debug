from typing import *
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for curr in range(len(nums)):
            for before in range(curr):
                if nums[before] < nums[curr]:
                    dp[curr] = max(dp[curr], dp[before] + 1)
        return max(dp)


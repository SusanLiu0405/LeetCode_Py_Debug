from typing import List

# 其实就是二分查找一个list里最小的值，返回就完事
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        left = 0
        right = len(nums) - 1
        if nums[right] > nums[left]:
            return nums[0]
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])


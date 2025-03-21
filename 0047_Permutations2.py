from typing import List


# 求：一个List里能出现的所有排列
# 每个排列都必须出现所有数字
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        self.recursion([False] * len(nums), nums, [], results)
        return results

    def recursion(self, used, nums, path, results):
        if len(path) == len(nums):
            results.append(path[:])
            return

        for i in range(len(nums)):
            curr_num = nums[i]
            if used[i]:
                continue
            if i - 1 >= 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                continue
            path.append(curr_num)
            used[i] = True
            self.recursion(used, nums, path, results)
            used[i] = False
            path.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        self.recursionUnique([False] * len(nums), nums, [], results)
        return results

    def recursionUnique(self, used, nums, path, results):
        if len(path) == len(nums):
            results.append(path[:])
            return

        for i in range(len(nums)):
            curr_num = nums[i]
            if used[i]:
                continue
            if i - 1 >= 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                continue
            path.append(curr_num)
            used[i] = True
            self.recursionUnique(used, nums, path, results)
            used[i] = False
            path.pop()

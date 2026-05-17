'''
给数组a[]，找满足条件的一对i,j, 满足i <= j, a[i] == a[j], 要maximize a[i] + a[i + 1] + … + a[j]
返回最大的sum对应的i，j
followup：严格O(1)的额外空间，复杂度允许高一点
'''
class Solution:
    def maxSubarray(self, nums):
        prefix_sum = [0]
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix_sum.append(total)

        max_sum = float('-inf')


        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    curr_sum = prefix_sum[j + 1] - prefix_sum[i]
                    if curr_sum > max_sum:
                        max_sum = curr_sum
                        result = (i, j)
        return result

    def maxSubarrayFollowUp(self, nums):
        max_sum = float('-inf')
        result = (-1, -1)
        for i in range(len(nums)):
            curr_sum = nums[i]
            for j in range(i + 1, len(nums)):
                curr_sum += nums[j]
                if nums[i] == nums[j] and curr_sum > max_sum:
                    print("curr_sum = ", curr_sum)
                    print("i = ",i)
                    print("j = ", j)
                    max_sum = curr_sum
                    result = (i, j)
        return result


sol = Solution()
nums = [-1, -5, 3, -5, 3, 10, 3]
print(sol.maxSubarray(nums))

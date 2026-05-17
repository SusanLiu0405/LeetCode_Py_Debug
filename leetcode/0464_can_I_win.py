class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False

        num_set = set()
        return self.dfs(num_set, maxChoosableInteger, desiredTotal, 0)

    def dfs(self, num_set, maxChoosableInteger, desiredTotal, curr_sum):
        for i in range(1, maxChoosableInteger + 1):
            if i in num_set:
                continue
            if curr_sum + i >= desiredTotal:
                return True
            num_set.add(i)
            if not self.dfs(num_set, maxChoosableInteger, desiredTotal, curr_sum + i):
                # num_set.remove(i)
                return True
            num_set.remove(i)
        return False
sol = Solution()
print(sol.canIWin(10, 40))
'''
maxChoosableIntegar = 10
desiredTotal = 40
dfs(num_set = {}, maxChoosableInteger = 10, desiredTotal = 40, curr_sum = 0)
num_set = {1}
curr_sum = 1
dfs(num_set = {1}, maxChoosableInteger = 10, desiredTotal = 40, curr_sum = 1)

'''
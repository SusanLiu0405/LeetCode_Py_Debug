from collections import Counter
# def wakeNumber(num) -> bool:
#     num = list(map(int, str(num)))
#     num_counter = Counter(num)
#     for i in range(len(num)):
#         if num[i] == 0:
#             return False
#         if num_counter[i] > 1:
#             return False
#         if i >= 2 and num[i - 1] < num[i] and num[i - 1] < num[i - 2]:
#             return False
#     return True
# print(wakeNumber(34321))

class Solution:
    def countPerfectWakeNumber(self, end_num):
        self.count = 0
        num_counter = set()
        self.dfs(0, end_num, num_counter, -1, -1)
        return self.count
    
    def dfs(self, start_num, end_num, num_counter, prev_1, prev_2):
        for digit in range(1, 10):
            if digit in num_counter:
                continue
            next_num = start_num * 10 + digit
            if next_num > end_num:
                continue
            if prev_2 != -1 and prev_1 != -1 and prev_1 < digit and prev_1 < prev_2:
                continue
            self.count += 1
            num_counter.add(digit)
            self.dfs(next_num, end_num, num_counter, digit, prev_1)
            num_counter.remove(digit)

sol = Solution()
print(sol.countPerfectWakeNumber(123))
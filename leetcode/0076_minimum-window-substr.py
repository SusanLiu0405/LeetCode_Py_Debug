from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        needs = Counter(t)
        missing = len(t) 
        left = 0
        best_len = float('inf')
        best_left = 0
        for right, char in enumerate(s):
            if needs[char] > 0:
                missing -= 1
            needs[char] -= 1

            while missing == 0:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                left_char = s[left]
                needs[left_char] += 1
                if needs[left_char] > 0:
                    missing += 1
                left += 1

        if best_len == float('inf'):
            return ""
        else:
            return s[best_left: best_left + best_len]
sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s, t))
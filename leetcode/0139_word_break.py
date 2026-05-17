from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        return self.dfs(wordSet, s, 0)


    def dfs(self, wordSet, s, idx):
        if idx == len(s):
            return True

        for i in range(idx, len(s)):
            curr_word = s[idx: i + 1]
            if curr_word in wordSet:
                wordSet.remove(curr_word)
                flag = self.dfs(wordSet, s, i + 1)
                if flag:
                    print(wordSet)
                    print(idx)
                    return True
                wordSet.add(curr_word)
        return False

sol = Solution()
s = "abcd"
wordDict = ["a","ab","bcd","cd"]
print(sol.wordBreak(s, wordDict))
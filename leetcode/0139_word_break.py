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
                wordSet.add(curr_word)
                if flag:
                    return True
                
        return False
'''
        hashset int 
浅拷贝            1
深拷贝      1

浅拷贝只copy引用（地址），不copy对象
深拷贝：重新创建一个一模一样的对象
'''
sol = Solution()
s = "abcd"
wordDict = ["a","ab","bcd","cd"]
print(sol.wordBreak(s, wordDict))
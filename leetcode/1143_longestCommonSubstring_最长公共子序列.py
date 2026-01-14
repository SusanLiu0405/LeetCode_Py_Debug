def longestCommonSubsequence(text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if text1[i] == text2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[rows - 1][cols - 1]
text1 = "abcdjw"
text2 = "3830v29w"
print(longestCommonSubsequence(text1, text2))







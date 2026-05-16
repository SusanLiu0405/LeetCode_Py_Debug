from typing import List
class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_length = 0

        if not matrix or not matrix[0]:
            return max_length
        row = len(matrix)
        col = len(matrix[0])

        visited_board = [[False] * col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                length = self.dfs(matrix, i, j, -1, visited_board)
                max_length = max(length, max_length)
        return max_length

    def dfs(self, matrix, i, j, last_value, visited_board):
        row = len(matrix)
        col = len(matrix[0])

        if i < 0 or i >= row or j < 0 or j >= col or last_value > matrix[i][j]:
            return 0
        if visited_board[i][j]:
            return 0
        visited_board[i][j] = True
        curr_max = 1
        curr_max = max(1 + self.dfs(matrix, i + 1, j, matrix[i][j], visited_board), curr_max)
        curr_max = max(1 + self.dfs(matrix, i - 1, j, matrix[i][j], visited_board), curr_max)
        curr_max = max(1 + self.dfs(matrix, i, j + 1, matrix[i][j], visited_board), curr_max)
        curr_max = max(1 + self.dfs(matrix, i, j - 1, matrix[i][j], visited_board), curr_max)
        visited_board[i][j] = False
        return curr_max
    
solution = Solution()
matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(solution.longestIncreasingPath(matrix))
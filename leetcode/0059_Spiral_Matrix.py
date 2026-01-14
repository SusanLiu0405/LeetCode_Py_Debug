from typing import *

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        outputMatrix = [[0 for _ in range(n)] for _ in range(n)]
        step = n * n
        top, bottom, left, right = 0, n - 1, 0, n - 1

        if not outputMatrix:
            return outputMatrix
        # 右下左上跑，跑完就缩圈，剩余单行列，直接遍历完
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                step -= 1
                outputMatrix[top][i] = n * n - step

            for i in range(top + 1, bottom + 1):
                step -= 1
                outputMatrix[i][right] = n * n - step

            for i in range(right - 1, left - 1, -1):
                step -= 1
                outputMatrix[bottom][i] = n * n - step

            for i in range(bottom - 1, top, -1):
                step -= 1
                outputMatrix[i][left] = n * n - step

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return outputMatrix

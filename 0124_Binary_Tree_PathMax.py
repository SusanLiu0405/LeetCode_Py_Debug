from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        self._maxPathSumHelper(root)
        return self.max_sum

    def _maxPathSumHelper(self, node):
        if not node:
            return 0
        left_sum = max(0, self._maxPathSumHelper(node.left))
        right_sum = max(0, self._maxPathSumHelper(node.right))
        self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
        return node.val + max(left_sum, right_sum)

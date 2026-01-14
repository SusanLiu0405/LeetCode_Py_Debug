from collections import deque
from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            curr_level = []
            level_len = len(queue)
            level_max = float('-inf')
            for i in range(level_len):
                curr_node = queue.popleft()
                level_max = max(curr_node.val, level_max)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            result.append(level_max)

        return result
from typing import *
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # early exit
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            curr_level = []
            level_len = len(queue)
            for i in range(level_len):
                curr_node = queue.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            result.append(curr_level)

        return result

# 创建Solution实例
sol = Solution()

# 构建二叉树
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# 调用levelOrder函数
print(sol.levelOrder(root))

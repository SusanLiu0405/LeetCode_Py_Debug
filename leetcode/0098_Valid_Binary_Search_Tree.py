from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            # 对于左子树，上限变为当前节点的值；对于右子树，下限变为当前节点的值
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False

            return True

        return helper(root)
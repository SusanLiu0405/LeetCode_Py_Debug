from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def orderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
	# call different orders here:
        self.recursion(root, result)
        return result
    
    def recursion_preorder(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return result
        result.append(node.val)
        self.recursion_preorder(node.left, result)
        self.recursion_preorder(node.right, result)
        
    def recursion_in_order(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return result
        self.recursion_in_order(node.left, result)
        result.append(node.val)
        self.recursion_in_order(node.right, result)
    def recursion_post_order(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return result
        self.recursion_post_order(node.left, result)
        self.recursion_post_order(node.right, result)
        result.append(node.val)

from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        results = []
        self.dfs(root, [], results)
        return results

    def dfs(self, node, path, results):
        path.append(node.val)
        if not node.left and not node.right:
            #叶子结点
            self.addPath(path, results)
            path.pop()
            return
        if node.left:
            self.dfs(node.left, path, results)
        if node.right:
            self.dfs(node.right, path, results)
        path.pop()
        
    def addPath(self, path, results):
        results.append("->".join([str(i) for i in path]))


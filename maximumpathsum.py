from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:return 0
            lMax = dfs(node.left)
            rMax = dfs(node.right)

            lMax = max(lMax, 0)
            rMax = max(rMax, 0)
            
            res[0] = max(res[0], node.val + lMax + rMax)

            return node.val + max(lMax, rMax)
        dfs(root)
        return res[0]
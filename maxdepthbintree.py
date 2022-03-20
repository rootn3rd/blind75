from collections import deque
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + (self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthBfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])

        while queue:

            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1
        return level

    def maxDepthDfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [(root, 1)]

        while queue:

            node, depth = queue.pop()

            if node:
                res = max(res, depth)
                if node.right:
                    queue.append((node.right, depth+1))
                if node.left:
                    queue.append((node.left, depth + 1))

        return res

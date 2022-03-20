from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []
        while q:
            temp = []
            children = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            
            res.append(temp)
            q = children
        return res
        


from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1: mid + 1], inorder[: mid])
        node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return node


def printTree(node):
    if not node:
        return
    print(node.val, end=" ")
    printTree(node.left)
    printTree(node.right)

sol = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
ret = sol.buildTree(preorder, inorder)
printTree(ret)


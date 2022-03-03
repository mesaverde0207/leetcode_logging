# https://leetcode.com/problems/inorder-successor-in-bst/
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
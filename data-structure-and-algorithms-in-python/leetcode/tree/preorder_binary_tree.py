# https://leetcode.com/problems/binary-tree-preorder-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root):
        if root:
            self.result.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
            return self.result

# https://leetcode.com/problems/path-sum/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True if root.val == sum else False
        if self.has_path_sum(root.left, sum - root.val):
            return True
        if self.has_path_sum(root.right, sum - root.val):
            return True
        return False

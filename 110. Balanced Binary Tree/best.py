# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC: O(N)
# SC: O(N)
# It breaks out the moment we find a non-balanced subtree using try except we raise an error

class Solution:
    def isBalanced(self, root):

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left-right) > 1:
                raise ValueError

            return 1 + max(left, right)

        try:
            dfs(root)
            return True
        except ValueError:
            return False

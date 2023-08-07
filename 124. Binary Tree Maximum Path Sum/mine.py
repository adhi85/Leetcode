# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        # TC: O(N)
        maxs = root.val

        def dfs(node, s):
            nonlocal maxs
            if not node:
                return 0

            left = dfs(node.left, s)
            right = dfs(node.right, s)

            s = s + node.val + max(left, right, 0)
            maxs = max(maxs, s, left+right+node.val)

            return s

        dfs(root, 0)
        return maxs
# TC: O(N)

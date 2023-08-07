# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):

        maxs = [root.val]

        # Checking entire tree
        def dfs(node):
            if not node:
                return 0

            # Getting the left and right side max path sum ==> If the left and right
            # is negative then we'll take 0 because adding a negative value will only make it lesser 
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # left = max(left,0)
            # right = max(right,0)

            # Updating the max value with every Split path
            maxs[0] = max(maxs[0], node.val+left+right)

            return node.val + max(left, right)

        dfs(root)
        return maxs[0]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxi):
            count = 0
            if not root:
                return 0

            if root.val >= maxi:
                count += 1
                maxi = root.val

            count += dfs(root.left, maxi)
            count += dfs(root.right, maxi)

            return count

        return dfs(root, root.val)

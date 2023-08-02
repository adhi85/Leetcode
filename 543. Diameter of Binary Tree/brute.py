# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):

        if not root:
            return 0

        ld = self.diameterOfBinaryTree(root.left)
        rd = self.diameterOfBinaryTree(root.right)

        cur = self.maxDepth(root.left) + self.maxDepth(root.right)

        return max(cur, max(ld, rd))

    def maxDepth(self, root):

        if not root:
            return 0

        left = 1 + self.maxDepth(root.left)
        right = 1 + self. maxDepth(root.right)

        return max(left, right)

# TC: O(N^2)
# SC: O(1)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root):
        maxD = [0]

        self.findMax(root, maxD)
        return maxD[0]

    def findMax(self, root, maxD):
        if not root:
            return 0

        lh = self.findMax(root.left, maxD)
        rh = self.findMax(root.right, maxD)

        maxD[0] = max(maxD[0], lh+rh)

        return 1 + max(lh, rh)

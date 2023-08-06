# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):

        def inorder(root):
            el = []

            if root.left:
                el += inorder(root.left)

            el.append(root.val)

            if root.right:
                el += inorder(root.right)

            return el

        x = inorder(root)

        return x[k-1]

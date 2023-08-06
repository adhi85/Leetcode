# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):

        def inorder(node):
            ele = []

            if node.left:
                ele += inorder(node.left)
            ele.append(node.val)

            if node.right:
                ele += inorder(node.right)

            return ele

        x = inorder(root)
        y = sorted(x)

        if len(set(x)) != len(y):
            return False

        return x == y

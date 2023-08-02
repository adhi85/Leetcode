# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):

        def postorder(root):
            elements = []

            if root:
                elements += postorder(root.left)
                elements += postorder(root.right)
                elements.append(root.val)

            else:
                elements.append(None)

            return elements

        return postorder(p) == postorder(q)

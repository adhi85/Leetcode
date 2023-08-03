# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root, subRoot):

        def isSame(p, q):
            if p == None or q == None:
                return p == q

            return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)

        def dfs(root, subRoot):
            if not root:
                return False

            return isSame(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)

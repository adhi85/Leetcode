from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum):

        if not root:
            return False

        q = deque([(root, targetSum-root.val)])

        while q:

            node, curSum = q.popleft()

            if not node.left and not node.right and curSum == 0:
                return True

            if node.left:
                q.append((node.left, curSum-node.left.val))
            if node.right:
                q.append((node.right, curSum-node.right.val))

        return False

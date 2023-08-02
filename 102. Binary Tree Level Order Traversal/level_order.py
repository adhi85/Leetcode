from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):

        if not root:
            return None

        q = deque([root])
        ans = []

        while q:
            size = len(q)

            level = []

            for i in range(size):
                x = q.popleft()
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                level.append(x.val)
            ans.append(level)
        return ans

# TC: O(N)
# SC: O(N)
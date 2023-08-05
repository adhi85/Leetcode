from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        if not root:
            return None

        ans = []
        q = deque([root])

        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                temp.append(node.val)
            ans.append(temp)

        res = []

        for i in ans:
            res.append(i[-1])
        return res

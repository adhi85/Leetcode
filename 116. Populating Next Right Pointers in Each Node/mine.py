from collections import deque
# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return None

        curr = root
        q = deque([curr])

        while q:
            z = len(q)-1
            for i in range(len(q)):
                node = q.popleft()

                if z:
                    node.next = q[0]
                    z -= 1
                else:
                    node.next = None

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
# TC:O(N)
# SC:O(N)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k: int) -> int:

        n = 0
        stack = []
        curr = root
        
        while curr or stack:
        # Traversing all the way to left until we get none and adding to stack
            while curr:
                stack.append(curr)
                curr = curr.left
        # Getting the last element in stack i.e least element in BST
            curr = stack.pop()
            # Add n so that we can knowif we got the kth element
            n += 1

            if n == k:
                return curr.val
        # Go to right since left became none and then continue going left to get min element
            curr = curr.right
# TC: O(N)
# SC: O(N)

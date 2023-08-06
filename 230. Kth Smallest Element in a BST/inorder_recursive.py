# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):

        # Making it global to be used in inorder function
        self.k = k
        self.ans = 0
        # Calling inorder function and it will update the ans
        self.inorder(root)
        
        return self.ans

    def inorder(self, root):

        if not root:
            return

        # Since find min go to  last of left node
        self.inorder(root.left)

        # decrease k once if we find the least element
        self.k -= 1

        # if k zero means we found kth element
        if not self.k:
            # So make ans as the value of that root
            self.ans = root.val
            return

        # Call the same on right
        self.inorder(root.right)

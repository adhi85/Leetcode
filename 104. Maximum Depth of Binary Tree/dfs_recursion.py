# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        
        
        # TC: O(N)
        if not root:
            return 0
        
        leftmax =1 + self.maxDepth(root.left)
        rightmax = 1 + self.maxDepth(root.right)
        
        return max(leftmax,rightmax)
        
        
                

                
        
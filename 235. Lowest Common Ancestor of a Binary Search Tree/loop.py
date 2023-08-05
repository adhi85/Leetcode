# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # TC: O(logN)
        # SC: O(1)
        curr = root
        
        while curr:
            if (p.val<=curr.val<=q.val) or (q.val<=curr.val<=p.val):
                return curr
            
            elif (p.val<curr.val) and q.val<curr.val:
                curr = curr.left
            else:
                curr = curr.right
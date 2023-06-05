# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        elements = []
        
        if not root:
            return None
        
        if root.left:
            elements += self.postorderTraversal(root.left)
            
        
        if root.right:
            elements += self.postorderTraversal(root.right)
            
        elements.append(root.val)
        
        return elements
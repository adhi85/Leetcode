# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.ptr = -1
        self.lis = self.inorder(root)
        
    def next(self) -> int:
        self.ptr +=1
        return self.lis[self.ptr]

    def hasNext(self) -> bool:
        return self.ptr<len(self.lis)-1
        
    
    def inorder(self,root):
        
        elements = []
        
        if root.left:
            elements += self.inorder(root.left)
            
        elements.append(root.val)
        
        if root.right:
            elements += self.inorder(root.right)
            
        return elements


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
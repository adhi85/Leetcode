
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root, subRoot):

        def postorder(root):
            el = []

            if root:
                el += postorder(root.left)
                el += postorder(root.right)
                el.append(root.val)
            else:
                el.append(None)

            return el

        rl = postorder(root)
        srl = postorder(subRoot)
        if rl == srl:
            return True

        i, j = 0, len(srl)

        while j < len(rl):
            if rl[i:j] == srl:
                return True
            i += 1
            j += 1
        return False

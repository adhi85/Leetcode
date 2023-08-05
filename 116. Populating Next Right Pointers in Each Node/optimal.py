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

        head = root

        while root:
            curr, root = root, root.left

            while curr:
                if curr.left:
                    curr.left.next = curr.right

                    if curr.next:
                        curr.right.next = curr.next.left
                else:
                    break
                curr = curr.next
        return head

        #     if not root: return None

        # head = root

        # while root:
        #     curr , root = root , root.left

        #     while curr:
        #         if curr.left:
        #             curr.left.next = curr.right
        #             if curr.next:
        #                 curr.right.next = curr.next.left
        #         else:
        #             break
        #         curr = curr.next

        # return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):  
        if head:
                prev = None
                current = head
                nextptr = head.next

                while current:
                    nextptr = current.next
                    current.next = prev
                    prev = current
                    current = nextptr
                head = prev

                return head
        return None
    
# TC: O(N)
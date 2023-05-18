# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        
        slow = fast = head
        
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
    
# TC: O(n)
# SC: O(1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        
        # If list is None or only one element
        if not head or not head.next:
            return None
        
        # Run loop until slow == fast to find collision
        # If loop is not there stop when fast is last node or NONE 
        while fast and fast.next  :
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # If fast is None or fast is last element No loop is present
        if not fast or not fast.next:
            return None
        
        # Reassign slow to head to start iterating from start to find the cycle start
        slow = head
        
        # Move both slow and fast only by one step until they collide
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        # return the collided element
        return slow
        
        
        
        
        
        
        
        

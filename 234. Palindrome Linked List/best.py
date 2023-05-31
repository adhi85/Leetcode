# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head):
        slow = head
        fast = head
        
        # If length = 1 or head is None
        if not head or not head.next:
            return True
        
        # finding the middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reversing the Linked list from slow.next to end
        prev,current = None,slow.next
        while current:
            prev, current.next, current = current, prev, current.next
            # nextptr = current.next
            # current.next = prev
            # prev = current 
            # current = nextptr
        slow.next = prev
        
        # Comparing elements starting new from head and reversed list from slow.next
        new,slow = head,slow.next 
        
        while slow:
            if new.val != slow.val:
                return False
            new= new.next
            slow= slow.next
            
        return True
            
# TC: O(N/2)[finding middle] + O(N/2)[Reversing the half sublist] + O(N/2)[Comparing the elements]
# SC: O(1)        


            
        
        
        
        
        
        
        
        
        
        
        
        

        
            
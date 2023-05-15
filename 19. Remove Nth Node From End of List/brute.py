# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head,n):
        def get_length(ptr):
            count = 0
            while ptr:
                count+=1
                ptr = ptr.next
            return count
                
        length = get_length(head) - n 
        ptr = head
        
        if length == 0:
            head = head.next
            return head
        
        for i in range(0,length-1):
            ptr = ptr.next
    
        ptr.next = ptr.next.next
        
        return head
            
# TC: O(2*n)         

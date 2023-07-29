# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        
        def reverse(head):
            prev = None
            temp = head
            
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            return prev
        
        
        head = reverse(head)
        temp = head
        
        if n ==1:
            head= head.next
        else:
            while (n-1):
                prev = temp
                temp = temp.next
                n -=1
            prev.next = temp.next
            
        head = reverse(head)
        
        return head
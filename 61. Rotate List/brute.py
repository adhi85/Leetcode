# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):

        if not head or not head.next or k==0:
            return head
    
        # Worst case is O(k * N)
        while(k):
            temp = head
            
            # O(N)
            while temp.next.next:
                temp = temp.next
            
            temp.next.next = head
            head = temp.next
            temp.next = None
            
            k-=1
        return head
                
# TC: O(k*N)
# SC: O(1)
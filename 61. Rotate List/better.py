# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):

        if not head or not head.next or k==0:
            return head
        
        temp1 = head
        len = 0

        #O(N)
        while temp1:
            temp1 = temp1.next
            len+=1

        # Worst case is O(len) ie O(N)
        while(k%len):
            temp = head
            
            # O(N)
            while temp.next.next:
                temp = temp.next
            
            temp.next.next = head
            head = temp.next
            temp.next = None
            
            k-=1
        return head
                
# TC: O(N) + O(N^2)
# SC : O(1)
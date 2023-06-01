# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):

        def get_length(head):
            count = 0
            while head:
                count+=1
                head = head.next
                
            return count
        
        # Return head itself if empty list or single element
        if not head or not head.next or k == 0:
            return head
        
        # Compute length O(n) and actual rotation after looping
        length = get_length(head)
        rotation = k % length
        
        # No need to perform any function
        if rotation == 0:
            return head
        
        # Go to last node and point it to head        
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = head

        # Go to actual Last node (Means until where the list should end after rotation)
        for i in range(length-rotation):
            temp = temp.next
        
        # change head to new head
        head = temp.next

        # Make it last node
        temp.next = None

        return head

# TC: O(N) + O(N) + O(N-k)
# SC : O(1)



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):

        def get_length(head):
            count = 0
            ptr = head
            while ptr:
                count += 1
                ptr = ptr.next
            return count
        length = get_length(head)
        middle =  length//2 + 1
        
        for i in range(middle-1):
            head = head.next
        return head
            
# TC: O(n) +O(n/2)        

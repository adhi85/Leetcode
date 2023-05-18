# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        
        temp1 = head
        hashset = set()
        
        while temp1:
            if temp1 in hashset:
                return True
            hashset.add(temp1)
            temp1 = temp1.next
        return False
    
# TC : O(n)
# SC: O(n)
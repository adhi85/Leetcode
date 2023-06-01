# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        hashset = set()
        
        temp = head
        
        while temp:
            if temp in hashset:
                return temp
            hashset.add(temp)
            temp = temp.next
        return None
    
# TC: O(N)
# SC: O(N)
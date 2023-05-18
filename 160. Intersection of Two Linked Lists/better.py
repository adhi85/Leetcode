# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        temp1 = headA
        temp2 = headB
        
        hashset = set()
        
        while temp1:
            hashset.add(temp1)
            temp1 = temp1.next 
        while temp2:
            if temp2 in hashset:
                return temp2
            temp2 = temp2.next

# TC: O(n+m) in operator time complexity is O(1) mostly
# SC: O(n) 
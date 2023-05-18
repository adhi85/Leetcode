# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        temp1 = headA
        temp2 = headB
        
        while temp1:
            while temp2:
                if temp2 == temp1:
                    return temp1
                temp2 = temp2.next
                
            temp1 = temp1.next
            temp2 = headB

# TC: O(n * m) means we are iterating both the linked lists
# SC: O(1) 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        #Best
        
        def get_length(head):
            count = 0
            while head:
                count +=1
                head = head.next
            return count
        
        def traverse(head,num):
            for i in range(num):
                head = head.next
            return head
        
        temp1 = headA
        temp2 = headB
        diff = get_length(headA) - get_length(headB)
        
        if diff > 0:
            temp1 = traverse(temp1,abs(diff))
        else:
            temp2 = traverse(temp2,abs(diff))
        
        while temp1 and temp2:
            if temp1 == temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next

# TC: O(m+n)[for getting length ] + O(m-n)[for traversing] + O(n)
# SC: O(1)
            
        
        
        
        
        
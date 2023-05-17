# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        temp = ListNode()
        dummy = temp
        
        carry = 0
        
        while l1 or l2 or carry:
            smm = 0
            
            if l1!= None:
                smm += l1.val
                l1 = l1.next
            if l2 != None:
                smm += l2.val
                l2 = l2.next
            
            smm += carry
            carry = smm // 10

            n = ListNode(smm % 10)
            temp.next = n
            temp = n
            
        return dummy.next

        
            
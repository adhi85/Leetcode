# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1,list2):
        list3 = ListNode()
        dd = list3
        while list1 and list2:
            if list1.val <= list2.val:
                node = ListNode(list1.val)
                list3.next = node
                list3 = node
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list3.next = node
                list3 = node
                list2 = list2.next

        while list1:
            node = ListNode(list1.val)
            list3.next = node
            list3 = node
            list1 = list1.next
        while list2:
            node = ListNode(list2.val)
            list3.next = node
            list3 = node
            list2 = list2.next           
        
        head  = dd.next
        return head
    
# TC: O(n+m)
# SC: O(n+m)
                
        
        
        

                
                
            
                
        
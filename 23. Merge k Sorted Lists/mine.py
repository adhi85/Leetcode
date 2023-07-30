# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):

        values = []
        for i in lists:

            temp = i

            while temp:
                values.append(temp.val)
                temp = temp.next

        values.sort()

        dummy = ListNode()
        head = dummy

        for i in values:
            new = ListNode(i)
            head.next = new
            head = head.next

        return dummy.next
    
# TC: O(nlogn)
# SC: O(n)

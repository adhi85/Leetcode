# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(prev, head):
            temp = head

            while temp:
                temp = head.next
                head.next = prev
                prev = head
                head = temp

            return prev

        size = 0
        temp = head

        while temp:
            temp = temp.next
            size += 1

        if size == 1:
            return head

        temp = head

        for i in range(size//2):
            prev = temp
            temp = temp.next

        last = reverse(prev, temp)
        first = head

        while first != last:

            temp = first.next
            first.next = last
            first = temp
            temp = last.next
            last.next = first
            last = temp

        last.next = None

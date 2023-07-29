# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        size = 0

        temp = head

        while temp:
            temp = temp.next
            size += 1

        stack = []
        temp = head
        i = 0

        for i in range(size//2):
            temp = temp.next

        while temp:
            stack.append(temp)
            temp = temp.next

        dummy = head

        for i in range(size//2):
            temp = dummy.next
            dummy.next = stack.pop()
            dummy = dummy.next
            dummy.next = temp
            dummy = dummy.next

        dummy.next = None

# TC : O(N)
# SC : O(N)

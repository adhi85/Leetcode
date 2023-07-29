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

        slow, fast = head, head.next

        # Finding Middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing
        last, prev = slow.next, None

        while last:
            temp = last.next
            last.next = prev
            prev = last
            last = temp

        # Joining
        first, last = head, prev
        slow.next = None

        while last:
            temp1, temp2 = first.next, last.next
            first.next = last
            last.next = temp1
            first, last = temp1, temp2

# TC: O(N)
# SC: O(1)
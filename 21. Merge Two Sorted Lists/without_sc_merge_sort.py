class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        if not list1:
            return list2

        if not list2:
            return list1

        i = list1
        j = list2

        head = ListNode()
        temp = head
        while i and j:

            if i.val <= j.val:
                temp.next = i
                temp = i
                i = i.next
            else:
                temp.next = j
                temp = j
                j = j.next

        if i:
            temp.next = i
        else:
            temp.next = j
        # while i:
        #     temp.next = i
        #     temp = i
        #     i = i.next
        # while j:
        #     temp.next = j
        #     temp = j
        #     j = j.next

        return head.next

"""Definition for a Node. """
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head:
            return head
        
        temp = head
        
        # Creating new deep copy nodes in-between real nodes
        while temp:
            new = Node(temp.val)
            new.next = temp.next
            temp.next = new
            temp = temp.next.next
            
        # Pointing the deep copy nodes to their own randoms
        temp = head
        
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
            # try:
            #     temp.next.random = temp.random.next
            # except:
            #     temp.next.random = None
            # temp = temp.next.next
        
        # Seperating the deep copy and real nodes
        
        dummy = Node(0)
        new_Head = dummy 
        first = head
        
        while first:
            second = first.next.next
            dummy.next = first.next
            first.next = second
            dummy = dummy.next
            first = second

        
        return new_Head.next
            
# TC: O(N) + O(N) + O(N) = O(N)
# SC: O(1)            
            
            
            
        
            
        
        
        
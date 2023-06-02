# Definition for a Node
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        hashmap = {}
        temp = head
        
        if not head:
            return head
        
        while temp:
            hashmap[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        
        while temp:
            hashmap[temp].next = hashmap.get(temp.next)
            hashmap[temp].random = hashmap.get(temp.random)
            temp = temp.next
            
        return hashmap[head]
    
# TC: O(N) + O(N)
# SC: O(N)

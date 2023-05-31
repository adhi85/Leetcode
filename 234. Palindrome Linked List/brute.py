# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        sample = []
        
        temp = head
        
        while temp:
            sample.append(temp.val)
            temp = temp.next
        
        return sample == sample[::-1]
            
# TC: O(N) + O(N)=>reverse the list + O(N)=>compare both lists 
# SC: O(N) 

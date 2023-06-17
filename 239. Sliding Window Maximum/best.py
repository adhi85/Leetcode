from collections import deque
class Solution:
    def maxSlidingWindow(self, nums,k):
        
        stack = deque()
        
        ans = []
        
        # Arrangin the deque in deceasing order 
        
        for i in range(len(nums)):
            
            # Removing the left-most element when it is out of the sliding window
            if stack and (stack[0] == i-k):
                stack.popleft()
                
            # If element in nums greater than element in stack remove the small elements from stack
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            
            # Appending the indexes to stack
            stack.append(i)
            
            # Only append the greatest element to stack after the first window
            if i >=k-1:
                ans.append(nums[stack[0]])
                
        return ans

# TC: O(N) = O(N) + O(N
# SC: O(K) 
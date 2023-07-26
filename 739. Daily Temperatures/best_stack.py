class Solution:
    def dailyTemperatures(self, temperatures):
        
        ans = [0] * len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            
            while stack and t > stack[-1][1]:
                stackInd , stackTemp = stack.pop()
                ans[stackInd] = i - stackInd
            
            stack.append((i,t))
        
        return ans
# TC: O(N)
# SC: O(N)
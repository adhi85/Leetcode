class Solution:
    def dailyTemperatures(self, temperatures):

        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                stackInd = stack.pop()
                ans[stackInd] = i - stackInd
                
            stack.append(i)

        return ans
# TC:O(N)
# SC:O(N)

from collections import deque
class Solution:
    def largestRectangleArea(self, heights):
        
        stack = deque()

        leftSmall = []
        rightSmall = [0] * len(heights)

        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if not stack:
                leftSmall.append(0)
            else:
                leftSmall.append(stack[-1] + 1)
            stack.append(i)

        stack = deque()

        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if not stack:
                rightSmall[i] = len(heights)-1
            else:
                rightSmall[i] = stack[-1] -1 
            stack.append(i)
            
            
        maxArea = 0
        for i in range(len(heights)):
            area = (rightSmall[i] - leftSmall[i] + 1 ) * heights[i]
            maxArea = max(maxArea, area)
            
        return maxArea
        
        
        
        
        

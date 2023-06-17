class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        
        maxA = 0
        n = len(heights) 
        
        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]] >= heights[i]):
                height = heights[stack[-1]]
                stack.pop()
                
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxA  = max(maxA, width*height)
                
            stack.append(i)
        
        return maxA

# TC: O(N)
# SC: O(N) for stack
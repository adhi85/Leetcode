class Solution:
    def largestRectangleArea(self, heights) -> int:
        heights.append(0)
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                indx, height = stack.pop()
                width = (i - indx)

                area = width * height

                maxArea = max(area, maxArea)

                start = indx
            stack.append((start, h))

        # for i,h in stack:
        #     maxArea = max(maxArea, h * (len(heights)-i))

        return maxArea
    
# TC: O(N)
# SC: O(N)

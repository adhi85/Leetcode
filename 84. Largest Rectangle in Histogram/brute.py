def largestRectangleArea(self, heights):

    maxs = 0

    # TC: O(N^2)
    for i in range(len(heights)):
        left = i - 1
        right = i + 1

        s = heights[i]

        while left >= 0:
            if heights[left] >= heights[i]:
                s += heights[i]
                left -= 1
            else:
                break
        while right < len(heights):
            if heights[right] >= heights[i]:
                s += heights[i]
                right += 1
            else:
                break
        maxs = max(s, maxs)

    return maxs

# TC: O(N^2)
# SC:O(1)

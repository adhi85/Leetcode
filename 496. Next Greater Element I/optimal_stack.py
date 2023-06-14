from collections import deque

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

ans = []
stack = deque()
mapping = {}

stack.append(nums2[0])

for i in range(len(nums2)):
    while stack and nums2[i] > stack[-1]:
        mapping[stack[-1]] = nums2[i]
        stack.pop()
    stack.append(nums2[i])

for i in stack:
    mapping[i] = -1

for i in nums1:
    ans.append(mapping[i])

print(ans)

# TC:O(N)
# SC:O(N)
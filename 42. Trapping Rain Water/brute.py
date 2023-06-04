def trap(height):

    trapped = 0

    for i in range(len(height)):
        left = max(height[:i+1])
        right = max(height[i:])

        taking = min(left, right)

        trapped += taking-height[i]

    return trapped

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(trap(height))

# TC : O(N^2) ==  O(N) => for iterating entire array * O(N) => for finding max()=>O(N) 
# SC: O(1)
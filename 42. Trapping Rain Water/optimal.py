def trap(height):
    
    leftmax = 0
    rightmax = 0
    left = 0
    right = len(height) -1 
    
    trapped = 0
    
    while left < right:
        if height[left] <= height[right]:
            if height[left] >= leftmax:
                leftmax = height[left]
            else:
                trapped += leftmax - height[left] 
            left +=1
        else:
            if height[right] >= rightmax:
                rightmax = height[right]
            else:
                trapped += rightmax - height[right]
            right -=1

                
    return trapped

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(trap(height))

# TC: O(N)
# SC: O(1)

    
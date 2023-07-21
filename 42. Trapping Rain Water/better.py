def trap(height):
    
    # Creating the prefix_max and suffix_max array
    max_el = height[0]
    max_el_suffix = height[-1]
    prefix_max = []
    suffix_max = []  

    i = 0
    j = -1       
    while i<len(height):
        if height[i] > max_el:
            max_el = height[i]
        prefix_max.append(max_el)
        i +=1

        if height[j] > max_el_suffix:
            max_el_suffix = height[j]
        suffix_max.append(max_el_suffix)
        j-=1
        
    suffix_max = suffix_max[::-1]
    

    # Calculating the water on top of each block and adding totally
    trapped = 0
    
    for i in range(len(height)):
        left = prefix_max[i]
        right = suffix_max[i]
        
        trapping = min(left,right)
        
        trapped += trapping - height[i]
        
    return trapped

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(trap(height))

    
# TC: O(N) == O(N) =>Creating array + O(N) => traversing
# SC: O(2N) prefix and suffix array 
    


        # prefix = []
        # postfix = [0 for i in range(len(height))]
        # trapped = 0
        # x = 0
        
        # for i in range(len(height)):
        #     x = max(x,height[i])
        #     prefix.append(x)
        
        # x = 0
        # for i in range(len(height)-1, -1, -1):
        #     x = max(x,height[i])
        #     postfix[i] = x
        
        # for i in range(len(height)):
        #     l = prefix[i]
        #     r = postfix[i]
            
        #     x = min(l,r)
        #     trap = x - height[i]
            
        #     trapped += trap
            
        # return trapped
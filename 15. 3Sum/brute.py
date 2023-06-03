def threeSum(nums):
    
    new = []
    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    new.append([nums[i],nums[j],nums[k]])
                    
    for i in new:
        i.sort()
    
    new = list(set(tuple(sublist) for sublist in new))

        
    return new

print(threeSum([-1,0,1,2,-1,-4]))

# TC: O(n^3) + O(m * 3log3) + O(m)
# SC: O(m) 
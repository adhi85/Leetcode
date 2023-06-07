def singleNonDuplicate(nums):
    low = 0
    high = len(nums) - 2
    
    while low <= high:
        mid = (low + high) >> 1
        
        if nums[mid] == nums[mid ^ 1]:
            low = mid + 1  
        else:
            high = mid -1   
        
            
    return nums[low]

nums = [1,1,2,2,3,4,4,8,8]

print(singleNonDuplicate(nums))
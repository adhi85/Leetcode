
def threeSum(nums):
    
    ans = set()
    
    for i in range(len(nums)):
        hashset = set()
        for j in range(i+1,len(nums)):
            if (-1*(nums[i] + nums[j])) in hashset:
                ans.add(tuple(sorted([nums[i],nums[j],(-1*(nums[i] + nums[j])) ])))
            else:
                hashset.add(nums[j])
                
    ans = list(list(sublist) for sublist in ans)
    
    return ans

print(threeSum([-1,0,1,2,-1,-4]))

# TC: O(n^2) + O(m)
# SC: O(m) + O(n)
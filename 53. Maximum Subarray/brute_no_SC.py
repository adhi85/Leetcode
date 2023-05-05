nums = [-2,1,-3,4,-1,2,1,-5,4]
maxl = min(nums)
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        suml = 0
        for k in range(i,j):
            suml+= nums[k]
            if(suml>maxl):
                maxl = suml

# TC: O(n^3) approx
print(maxl)
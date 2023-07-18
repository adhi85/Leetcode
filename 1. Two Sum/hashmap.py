nums = [2,7,11,15] 
target = 9

ad = {}

# for i,j in enumerate(nums):
#     ad[j] = i

for i in range(len(nums)):
    k = target - nums[i]
    if k in ad:
        print([i,ad[k]])
    else:
        ad[nums[i]] = i

# TC: O(N)
# SC: O(N)
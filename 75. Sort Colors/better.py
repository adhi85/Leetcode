nums = [2,0,2,1,1,0]

z=o=t=0

for i in nums:
    if i == 0:
        z += 1
    elif i == 1:
        o += 1
    else:
        t += 1

for i in range(z):
    nums[i] = 0
for i in range(z,z+o):
    nums[i] = 1
for i in range(z+o, z+o+t):
    nums[i] = 2

# TC: O(N)
print(nums)



    

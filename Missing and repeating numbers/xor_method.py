

nums = [4,3,6,2,5,5]

def getFirstSetBit(x):
    return x & ~(x-1)

x = 0
for i in range(len(nums)):
    x ^= nums[i]
for i in range(1,len(nums)+1):
    x ^= i

y=z=0

set_bit_no = getFirstSetBit(x)

for i in range(len(nums)):
    if(nums[i] & set_bit_no):
        y ^= nums[i]  
    else:
        z ^= nums[i]
        
for i in range(1,len(nums)+1):
    if(i & set_bit_no):
        y ^= i 
    else:
        z ^= i
# TC: O(n)
if(y in nums):
    print("miss : ", z, "repeat: ", y )
else:
    print("miss : ", y, "repeat: ", z )
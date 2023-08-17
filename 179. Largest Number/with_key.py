from functools import cmp_to_key

def compare(n1,n2):
    if n1 + n2 > n2 + n1:
        return -1
    else:
        return 1
    
nums = [10,2]

for i, n in enumerate(nums):
    nums[i] = str(n)
    

nums = sorted(nums,key=cmp_to_key(compare))

print(str(int("".join(nums))))
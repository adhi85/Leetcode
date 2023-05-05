nums = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = min(nums)
suml = 0
for i in range(len(nums)):
    if suml == 0:
        start = i
    suml += nums[i]
    if(suml>max_sum):
        max_sum = suml
        
        ans_start = start
        ans_end = i
    if suml<0:
        suml = 0

#Total TC: O(n)
print(max_sum)
print(nums[ans_start:ans_end])

    
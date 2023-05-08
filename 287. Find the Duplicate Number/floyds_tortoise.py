nums = [1,3,4,2,2]
#OPTIMAL TORTOISE AND HARE
slow = fast = nums[0]


while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    
    if slow == fast:
        break

slow = nums[0]

while slow != fast:
    slow = nums[slow]
    fast = nums[fast]

# TC: O(N)
# SC:O(1)
    
print(fast)
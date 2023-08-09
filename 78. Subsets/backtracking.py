nums = [1, 2, 3]
ans = []
subset = []
def dfs(i):

    if i >= len(nums):
        ans.append(subset.copy())
        return
    
    # Including the element
    subset.append(nums[i])
    dfs(i+1)

    # Not including the element
    subset.pop()
    dfs(i+1)

dfs(0)
print(ans)
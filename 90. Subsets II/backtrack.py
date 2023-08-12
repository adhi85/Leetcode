nums = [1, 2, 2, 3]

# Sorting because if we have to skip we need loop
nums.sort()

ans = []


def backtrack(index, subset):

    if index >= len(nums):
        # Copying because it will change otherwise
        ans.append(subset[::])
        return

    # All subsets that include nums[index]
    subset.append(nums[index])
    backtrack(index+1, subset)
    subset.pop()

    # All subsets that doesnot include nums[index]
    # Skipping the same elements
    while index + 1 < len(nums) and nums[index] == nums[index+1]:
        index += 1

    # Call backtrack again on i+1
    backtrack(index+1, subset)


backtrack(0, [])

print(ans)

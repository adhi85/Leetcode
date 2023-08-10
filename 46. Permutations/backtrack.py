nums = [1, 2, 3]

# TC: O(N * N!)
# SC: O(N!)
def permutations(nums):

    ans = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        # Pop the first element
        first_element = nums.pop(0)
        # Do permutation on the remaining nums
        sub_perm = permutations(nums)

        # Append the popped element to the sub permutations
        for perm in sub_perm:
            perm.append(first_element)

        # Put it in Ans using extend because we need the sub perms
        ans.extend(sub_perm)

        # Append the popped element to nums to continue the loop for all elements
        nums.append(first_element)

    return ans


print(permutations(nums))

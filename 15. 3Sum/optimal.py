def threeSum(nums):
    i = 0
    nums.sort()
    ans = []

    # Outer Loop O(N)
    while i < (len(nums)-1):
        if (i > 0) and (nums[i] == nums[i-1]):
            i += 1
            continue
        j = i+1
        k = len(nums)-1

        # Inner loop 1st (n-1) then (n-2) etc.. almost O(N)
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1

            elif sum < 0:
                j += 1
            else:
                k -= 1
        i += 1

    return ans


print(threeSum([-1, 0, 1, 2, -1, -4]))


# TC: O(N^2) + O(nlogn) => for sorting
# SC: O(m) for returning the solution

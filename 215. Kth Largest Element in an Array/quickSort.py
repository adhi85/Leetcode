# TC: O(N)-> Avg, O(n^2)-> Worst

class Solution:
    def findKthLargest(self, nums, k: int) -> int:

        def quickSelect(l, r):
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            ind = len(nums) - k

            nums[r], nums[p] = nums[p], nums[r]

            if ind == p:
                return nums[p]

            elif ind > p:
                return quickSelect(p+1, r)
            else:
                return quickSelect(l, p-1)

        return quickSelect(0, len(nums)-1)

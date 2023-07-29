class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:

            m1 = (l+r) >> 1
            m2 = half - (m1+1) - 1  # we have to get the index in  nums2

            l1 = nums1[m1] if m1 >= 0 else float("-inf")
            l2 = nums2[m2] if m2 >= 0 else float("-inf")
            r1 = nums1[m1+1] if m1+1 < len(nums1) else float("inf")
            r2 = nums2[m2+1] if m2+1 < len(nums2) else float("inf")

            if l1 <= r2 and l2 <= r1:
                # Even
                if not total % 2:
                    return (max(l1, l2) + min(r1, r2)) / 2
                # Odd
                return min(r1, r2)

            elif l1 > r2:
                r = m1-1
            else:
                l = m1+1
# TC: O(log(min(n,m)))

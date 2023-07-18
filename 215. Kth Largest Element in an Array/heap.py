import heapq
class Solution:
    def findKthLargest(self, nums,k) -> int:
                
        heapq.heapify(nums)
        
        largest = heapq.nlargest(k,nums)
        
        return largest[-1]
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        
        hashmap = {}
        
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        
        heap = [(v,k) for k,v in hashmap.items()]
        
        largest = heapq.nlargest(k,heap)
        
        ans = []
        
        for i in range(k):
            ans.append(largest[i][1])
        return ans
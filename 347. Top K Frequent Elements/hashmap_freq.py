class Solution:
    def topKFrequent(self, nums, k):
        hashmap = {}
        
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
            
        freq = [[] for i in range(len(nums)+1)]        
        
        for i in hashmap.keys():
            freq[hashmap[i]].append(i)
        
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                
                if len(ans) == k:
                    return ans
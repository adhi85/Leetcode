from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        hashmap = defaultdict(int)
        
        for i in nums:
            hashmap[i] += 1
            
        new = defaultdict(list)
        for i in hashmap.keys():
            new[hashmap[i]].append(i)
        
        ans = []
        j = k
        while k > 0:
            try:
                x = new.pop(max(new.keys()))
                ans += x
                k -=1
            except:
                break
        
        while len(ans) != j:
            ans.pop()
        
        return ans
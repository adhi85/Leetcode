class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s) ==1:
            return len(s)
        
        hashset = set()
                
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l +=1
            hashset.add(s[r])
            r +=1
            ans = max(ans, r-l)
            
        return ans

# TC: O(N)
# SC: O(1)
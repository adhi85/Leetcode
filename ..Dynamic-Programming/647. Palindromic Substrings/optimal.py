class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = 0
        for i in range(len(s)):
            
            ans += self.count(s,i,i)
            ans += self.count(s,i,i+1)
            
        return ans
    
    def count(self,s,l,r):
        
        res = 0
        
        while l>=0 and r< len(s) and s[l] == s[r]:
            res +=1
            l -=1
            r +=1
            
        return res
            
        

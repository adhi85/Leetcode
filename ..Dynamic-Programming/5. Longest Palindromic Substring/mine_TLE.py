class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ans = s[0]
        
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                
                if (s[i:j+1] == s[j:i-1:-1]) or (s[i:j+1] == s[j::-1]):
                    if len(ans)< len(s[i:j+1]):
                        ans = s[i:j+1]
                        
        return ans
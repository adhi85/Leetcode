class Solution:
    def fib(self, n: int) -> int:
        dp = [-1 for i in range(n+1)]
              
        def help(n):
            if n <=1:
                return n
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = help(n-1) + help(n-2)
            
            return dp[n]
    
        return help(n)
    
# TC: O(N)
# SC: O(N)
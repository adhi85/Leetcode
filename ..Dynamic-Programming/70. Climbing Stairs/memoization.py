class Solution:
    def climbStairs(self, n: int) -> int:
        # Either like this or with dictionary
        # dp = {1:1, 2:2}
        dp = [0 for i in range(n+1)]
        def climb(n):
            
            if n==1:return 1
            if n==2:return 2
            
            # if n in dp:
            #     return dp[n]
            # else: rest of code

            if dp[n] !=0:
                return dp[n]
            
            dp[n] = climb(n-1) +  climb(n-2)
        
            return dp[n]
        
        return climb(n)
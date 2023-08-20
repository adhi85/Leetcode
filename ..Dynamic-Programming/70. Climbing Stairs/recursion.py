class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climb(n):
            if n ==1 : return 1
            if n ==2 : return 2
            
            left = climb(n-1)
            right = climb(n-2)
            
            return left + right
        
        return climb(n)
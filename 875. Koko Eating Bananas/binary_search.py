import math

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        
        def isValid(m):
            temp = h
            for i in range(len(piles)):
                time = math.ceil(piles[i]/m)
                temp -= time
                
            if temp >=0 :
                return 1
            return 0
        
        if len(piles) == h:
            return max(piles)
                
        i , r = 1 , max(piles)
        
        while i <=r:
            m = (i +r) // 2
            
            x = isValid(m)
            
            if x:
                valid = m
                r = m-1
            else:
                i = m +1
        
        return valid
        
class Solution:
    def minCostClimbingStairs(self, cost):

        # TC: O(2^N)
                
        def solve(indx):
            
            if indx == 0 :
                return cost[0]
            
            if indx == 1:
                return cost[1]
            
            ans = cost[indx] + min(solve(indx-1),solve(indx-2))
            
            return ans
        
        n = len(cost)   
        ans = min(solve(n-1),solve(n-2))
        
        return ans
    
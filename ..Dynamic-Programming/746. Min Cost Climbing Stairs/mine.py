class Solution:
    def minCostClimbingStairs(self, cost):
        
        ans = [float("inf")]

        # TC: O(2^N)
        
        def dfs(indx,total):
            
            if indx >= len(cost):
                ans[0] = min(ans[0], total)
                return
            
            dfs(indx+1,total+cost[indx])
            dfs(indx+2,total+cost[indx])
                   
        dfs(0,0)
        dfs(1,0)
        
        return ans[0]
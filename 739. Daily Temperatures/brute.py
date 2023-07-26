class Solution:
    def dailyTemperatures(self, temperatures):
        
        
#         TC : O(N^2)
        ans = []
        
        for i in range(len(temperatures)):
            
            l = r = i
            
            while r <len(temperatures) and temperatures[r] <= temperatures[l] :
                r +=1
                
            if r == len(temperatures):
                ans.append(0)
            else:
                ans.append(r-l)
            
        return ans
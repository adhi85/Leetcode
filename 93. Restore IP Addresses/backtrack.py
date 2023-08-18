class Solution:
    def restoreIpAddresses(self, s: str):
        
        ans = []
        
        if len(s) > 12:
            return ans
        
        def backtrack(indx,dots,currIP):
            
            if dots == 4 and indx ==len(s):
                ans.append(currIP[:-1])
                return
            
            if dots>4:
                return
            
            for j in range(indx,min(indx+3,len(s))):
                
                if int(s[indx:j+1]) <= 255 and (indx==j or s[indx] != "0"):
                    temp = currIP
                    currIP = currIP + s[indx:j+1] + "."    
                    backtrack(j+1,dots+1,currIP)
                    currIP = temp
                    
        backtrack(0,0,"")
        return ans
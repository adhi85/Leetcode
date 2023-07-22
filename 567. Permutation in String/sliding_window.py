class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False
        
        hash1 = {}
        hash2 = {}
        
        l,r = 0,len(s1)-1

        for i in range(len(s1)):
            hash1[s1[i]] = 1 + hash1.get(s1[i], 0)
            
        for i in range(l,r+1):
                hash2[s2[i]] = 1 + hash2.get(s2[i], 0)
                
        while r < len(s2):
            
            if hash1 == hash2:
                return True 
            
            if hash2[s2[l]] >0:
                hash2[s2[l]] -=1
            
            if hash2[s2[l]] == 0: 
                hash2.pop(s2[l])
            r +=1
            l +=1
            
            if r == len(s2):
                continue
                
            hash2[s2[r]] = 1 + hash2.get(s2[r], 0)   
             
        return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hash1 = {}
        hash2 = {}

        
        for i in range(97,123):
            hash1[i] = 0
            hash2[i] = 0

        
        for i in range(len(s1)):
            hash1[ord(s1[i])] = 1 + hash1.get(ord(s1[i]))
            
        l = 0
        r = len(s1)-1
                
        for i in range(l,r+1):
            try:
                hash2[ord(s2[i])] = 1 + hash2.get(ord(s2[i]), 0)
            except:
                pass
        
        while r < len(s2):
        
            if hash1 == hash2:
                return True
            
            hash2[ord(s2[l])]-=1
            r +=1
            
            try:
                hash2[ord(s2[r])] = 1 + hash2.get(ord(s2[r]))
            except:
                pass
            l +=1
        
        return False
    
#  TC: O(N)
#  SC: O(N)
class Solution:
    def groupAnagrams(self, strs):
        new = []
        
        for i in range(len(strs)):
            x = ''.join(sorted(strs[i]))
            new.append(x)
            
        hashset = set() 
        
        for i in range(len(new)):
            ad = []
            for j in range(len(new)):
                if new[i] == new[j]:
                    ad.append(j)   
            hashset.add(tuple(ad))
        
        hashset = list(hashset)
        
        for i in range(len(hashset)):
            hashset[i] = list(hashset[i])
            
        
        for i in range(len(hashset)):
            for j in range(len(hashset[i])):
                hashset[i][j] = strs[hashset[i][j]]
        return hashset
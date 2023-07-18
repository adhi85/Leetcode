from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        dic = defaultdict(list)

        for i in strs:
            count = [0] * 26
            
            for s in i:
                count[ord(s) - ord("a")] += 1
            
            dic[tuple(count)].append(i)
            
        return dic.values()
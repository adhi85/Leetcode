class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        hash1 = {}
        l = 0
        r = len(s1)-1

        for i in range(len(s1)):
            hash1[s1[i]] = 1 + hash1.get(s1[i], 0)

        while r < len(s2):
            hash2 = {}

            for i in range(l, r+1):
                hash2[s2[i]] = 1 + hash2.get(s2[i], 0)

            r += 1
            l += 1

            if hash1 == hash2:
                return True
        return False

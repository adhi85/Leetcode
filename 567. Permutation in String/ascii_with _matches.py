class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        hash1, hash2 = {}, {}
        matches = 0

        for i in range(ord("a"), ord("z")+1):
            hash1[i] = 0
            hash2[i] = 0

        l = 0

        for i in range(len(s1)):
            hash1[ord(s1[i])] += 1
            hash2[ord(s2[i])] += 1

        for i in hash2.keys():
            if hash2[i] == hash1[i]:
                matches += 1

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r])

            hash2[index] += 1
            if hash2[index] == hash1[index]:
                matches += 1
            elif hash2[index] == hash1[index] + 1:
                matches -= 1

            index = ord(s2[l])
            hash2[index] -= 1
            if hash2[index] == hash1[index]:
                matches += 1
            elif hash2[index] == hash1[index] - 1:
                matches -= 1
            l += 1

        return matches == 26

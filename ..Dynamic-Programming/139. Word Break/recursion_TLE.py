class Solution:
    def wordBreak(self, s: str, wordDict):

        wordDict = set(wordDict)

        def dfs(indx):

            if indx == len(s):
                return True

            for i in range(indx+1, len(s)+1):

                if s[indx:i] in wordDict and dfs(i):
                    return True
            return False

        return dfs(0)


T = Solution()
s = "leetcode"
wordDict = ["leet", "code"]

print(T.wordBreak(s, wordDict))

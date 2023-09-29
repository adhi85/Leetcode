class Solution:
    def wordBreak(self, s: str, wordDict):

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    break

        return dp[0]


T = Solution()

s = "leetcode"
wordDict = ["leet", "code"]

print(T.wordBreak(s, wordDict))

class Solution:
    def numDecodings(self, s):

        # TC: O(N)

        dp = [0] * (len(s)+1)

        dp[len(s)] = 1

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

                if i+1 < len(s) and 0 < int(s[i:i+2]) < 27:
                    dp[i] += dp[i+2]

        return dp[0]


T = Solution()

s = "226"
print(T.numDecodings(s))

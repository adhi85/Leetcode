class Solution:
    def letterCombinations(self, digits: str):

        hashmap = ["", "", "abc", "def", "ghi",
                   "jkl", "mno", "pqrs", "tuv", "wxyz"]

        ans = []

        def dfs(comb, indx):

            if len(comb) == len(digits):
                ans.append(comb)
                return

            for c in hashmap[int(digits[indx])]:
                dfs(comb+c, indx+1)

        dfs("", 0)

        if digits:
            return ans

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # TC: O(N^2)
        '''
        We are taking every letter as center and checking if it is palindrome
        by going to both left and right 
        We have to do for both cases even length and odd length

        Also make a helper function

        '''

        ans = ""
        ansLen = 0

        for i in range(len(s)):

            # Odd length

            l = r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > ansLen:
                    ans = s[l:r+1]
                    ansLen = r-l+1

                l -= 1
                r += 1

            # Even
            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > ansLen:
                    ans = s[l:r+1]
                    ansLen = r-l+1
                l -= 1
                r += 1

        return ans

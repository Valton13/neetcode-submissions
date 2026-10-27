class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        idx = 0
        n = len(s)
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < n and s[r] == s[l]:
                if (r - l + 1)> reslen:
                    reslen = r-l+1
                    idx = l
                l -= 1
                r += 1
            l,r = i , i+1
            while l >= 0 and r < n and s[r] == s[l]:
                if (r - l + 1)> reslen:
                    reslen = r-l+1
                    idx = l
                l -= 1
                r += 1
        return s[idx:reslen+idx]


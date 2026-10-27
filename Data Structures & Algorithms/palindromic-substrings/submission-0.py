class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 
        for i in range(len(s)):
            res += self.noofpali(s,i,i)
            res += self.noofpali(s,i,i+1)
        return res
    def noofpali(self , s , l,r):
        res =0 
        while l>=0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
    
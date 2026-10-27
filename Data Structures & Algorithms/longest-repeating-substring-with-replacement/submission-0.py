class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq ={}
        l =0
        max_c =0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r] , 0)+1
            max_c = max(max_c , freq[s[r]])
            while (r-l+1) - max_c > k:
                freq[s[l]] -=1
                l +=1
            res = max(res , (r-l+1))
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        res =[]
        l= 0
        alpha_set =set()
        for r ,val in enumerate(s):
            while val in alpha_set:
                alpha_set.remove(s[l])
                l +=1
            alpha_set.add(s[r])
            max_len = max(max_len , r-l+1)
            
        return max_len    
     

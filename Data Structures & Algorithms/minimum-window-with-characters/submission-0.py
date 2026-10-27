class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        freqt , wins = {} , {}
        for q in t:
            freqt[q] = freqt.get(q,0)+1
        curr , need = 0, len(freqt)
        res = [-1,-1] 
        reslen = float('inf')
        l=0
        for r in range(len(s)):
            q = s[r]
            wins[q] = wins.get(q,0)+1
            if q in freqt and wins[q] == freqt[q]:
                curr +=1
            while curr == need:
                if reslen > (r-l+1):
                    res = [l,r]
                    reslen = r-l+1
                wins[s[l]] -=1
                if s[l] in freqt and wins[s[l]] < freqt[s[l]]:
                    curr -=1
                l +=1
        l,r  =res
        return s[l:r+1] if reslen != float('inf') else ""       


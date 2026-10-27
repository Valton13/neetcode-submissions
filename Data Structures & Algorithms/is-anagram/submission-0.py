class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0]*26
        for i in  range(len(t)):
            count[ord(s[i])-ord('b')] +=1
            count[ord(t[i])-ord('b')] -=1    
        for val in count:
            if val != 0:
                return False
        return True               
        
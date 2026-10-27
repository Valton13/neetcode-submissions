class Solution:
    def isValid(self, s: str) -> bool:
        new = []
        par = {'(':')' , '[':']','{':'}'}
        for p in s:
            if p in par:
                new.append(p)
            else:
                if not new or par[new.pop()] != p:
                    return False   
        return not new        
        
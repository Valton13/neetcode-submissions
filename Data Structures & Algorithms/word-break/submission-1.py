class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        meme = {len(s) : True}
        def dfs(i):
            if i in meme:
                return meme[i]
            for w in wordDict:
                if((i + len(w)) <= len(s) and w == s[i :i+len(w)]):
                    if dfs(i+len(w)):
                        meme[i] = True
                        return True
            meme[i] = False
            return False
        return dfs(0)
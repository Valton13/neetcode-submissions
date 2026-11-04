class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        meme = {}
        def dfs(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in meme:
                return meme[(i,j)]
            if text1[i] == text2[j] :
                meme[(i,j)] = dfs(i+1 ,  j+1) +1
            else:
                meme[(i,j)] = max(dfs(i+1 , j) , dfs(i,j+1))
            return meme[(i,j)]
        return dfs(0,0)
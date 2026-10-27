class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        meme = [-1]*n
        def dfs(i):
            k = 1
            if meme[i] != -1:
                return meme[i]
            for j in range(i+1 , n):
                if nums[j] > nums[i]:
                    k = max(k , dfs(j) +1)
            meme[i] = k
            return k
        return max(dfs(i) for i in range(n))
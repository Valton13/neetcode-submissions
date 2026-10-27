class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cmin = 1
        cmax =1
        for num in nums:
            tmp = cmax * num
            cmax = max(cmax * num , cmin * num ,num )
            cmin = min(cmin * num , num , tmp )
            res = max(res , cmax)
        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i , val in enumerate(nums):
            if val > 0:
                break
            if i>0 and  val == nums[i-1] :
                continue
            l ,r = i+1 , n-1
            while l<r:
                curr = val + nums[l] + nums[r]
                if curr > 0:
                    r -=1
                elif curr < 0:
                    l +=1
                else:
                    res.append([val,nums[l] , nums[r]])
                    l +=1
                    r -=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res                

        
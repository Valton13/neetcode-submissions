class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
           for j in range(i+1,n):
               if nums[i] + nums[j] == target:
                    return [i,j]
        return []            
            #my code above
        #indi ={}
      #  for i , num in enumerate(nums):
     ##       indi[num] = i
   #     for i , num in enumerate(nums) :
  #          diff = target - num
  ##          if diff in indi and indi[diff] != i:
   #             return [i,indi[diff]]  
  #      return []          
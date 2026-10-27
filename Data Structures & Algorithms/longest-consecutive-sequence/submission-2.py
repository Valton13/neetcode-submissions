class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqset = set(nums)
        big =0
        for num in nums:
            if (num-1) not in seqset:
                seq = 1
                while (num +seq) in seqset:
                    seq +=1
                big = max(big,seq) 
        return big           
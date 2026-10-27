class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = {}
        char_index ={}
       # for val in strs:
       #     if val in count:
     #           count[val] += 1
      #      else:
      #          count[val] =1    
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] +=1
            res[tuple(count)].append(s)
        return list(res.values())        
        


        
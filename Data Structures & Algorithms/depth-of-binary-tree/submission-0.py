# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        ki = [[root,1]]
        while ki:
            curr , depth = ki.pop()
            if curr:
                ki.append([curr.left,depth+1] )
                ki.append([curr.right,depth+1])
                res= max(res , depth)
        return res


        
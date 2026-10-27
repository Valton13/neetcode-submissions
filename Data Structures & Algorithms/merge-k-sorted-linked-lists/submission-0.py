# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        kikis = []
        for no in lists:
            while no:
                kikis.append(no.val)
                no = no.next
        kikis.sort()
        ans = ListNode(0)
        curr = ans
        for kiki in kikis:
            curr.next = ListNode(kiki)
            curr = curr.next
        return ans.next
        
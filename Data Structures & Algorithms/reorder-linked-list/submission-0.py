# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        kiki =[]
        cur = head
        while cur:
            kiki.append(cur)
            cur = cur.next
        l,r = 0 , len(kiki)-1
        while l < r:
            kiki[l].next = kiki[r]
            l +=1
            if l >= r:
                break
            kiki[r].next = kiki[l]
            r -=1
        kiki[l].next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        cur = head
        while cur:
            leng += 1
            cur = cur.next
        if (leng-n) == 0:
            return head.next
        cur = head
        for i in range(leng-1):
            if i+1 == (leng-n):#4-2 = 2 -> 2 we want 3 
                cur.next = cur.next.next
            cur = cur.next
        return head
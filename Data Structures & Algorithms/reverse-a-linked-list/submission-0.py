# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iter = head
        prev = None
        while iter:
            next = iter.next
            iter.next = prev
            prev = iter
            iter = next
        return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def listLength(serf, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        length = self.listLength(head)
        if n == length: return head.next

        steps = length - n - 1
        iter = head
        for i in range(steps):
            iter = iter.next

        iter.next = iter.next.next
        return head
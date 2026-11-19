# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        curr = head
        leftSide = None

        for i in range(left - 1):
            leftSide = curr
            curr = curr.next

        prev = None
        for i in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        if leftSide: leftSide.next = prev
        else: head = prev

        for i in range(right - left):
            prev = prev.next

        prev.next = curr

        return head
        